from django.test import TestCase
from django.contrib.auth.models import User
from .models import Ride

class RideModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='password')