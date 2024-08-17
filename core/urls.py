from django.urls import path, include
from .views import UserCreateView, CustomAuthToken, RideViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'rides', RideViewSet)

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('login/', CustomAuthToken.as_view(), name='user-login'),
    path('users/', include('core.urls_user')),
    path('api/', include(router.urls)),
]
