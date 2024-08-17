from django.contrib.auth.models import User
from rest_framework import generics, viewsets, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from django.contrib.auth import authenticate
from .serializers import UserSerializer, CustomAuthTokenSerializer, RideSerializer
from .models import Ride
from .matching import find_best_driver

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CustomAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid credentials'}, status=400)

class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        ride = Ride.objects.get(id=response.data['id'])

        best_driver = find_best_driver(ride)
        if best_driver:
            ride.driver = best_driver
            ride.status = 'accepted'
            ride.save()
            serializer = self.get_serializer(ride)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'No available drivers found'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def update_status(self, request, pk=None):
        ride = self.get_object()
        status = request.data.get('status')
        if status in dict(Ride.STATUS_CHOICES).keys():
            ride.status = status
            ride.save()
            serializer = self.get_serializer(ride)
            return Response(serializer.data)
        return Response({'error': 'Invalid status'}, status=400)
