# core/models.py
from django.db import models
from django.contrib.auth.models import User

class Ride(models.Model):
    rider = models.ForeignKey(User, related_name='rides', on_delete=models.CASCADE)
    driver = models.ForeignKey(User, related_name='assigned_rides', on_delete=models.SET_NULL, null=True, blank=True)
    pickup_location_lat = models.FloatField()
    pickup_location_lon = models.FloatField()
    dropoff_location_lat = models.FloatField()
    dropoff_location_lon = models.FloatField()
    status = models.CharField(max_length=20, default='requested')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    current_location = models.JSONField(null=True, blank=True)  # Example for storing current location

