from django.test import TestCase
from django.contrib.auth.models import User
from .models import Ride
from .matching import find_best_driver

class RideMatchingTestCase(TestCase):
    def setUp(self):
        self.rider = User.objects.create(username='rider', is_driver=False, latitude=40.7128, longitude=-74.0060)
        self.driver = User.objects.create(username='driver', is_driver=True, latitude=40.7138, longitude=-74.0070)
        self.ride = Ride.objects.create(
            rider=self.rider,
            pickup_location_lat=40.7127,
            pickup_location_lon=-74.0059,
            dropoff_location_lat=40.730610,
            dropoff_location_lon=-73.935242
        )

    def test_find_best_driver(self):
        best_driver = find_best_driver(self.ride)
        self.assertEqual(best_driver, self.driver)
