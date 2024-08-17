from celery import shared_task
from .models import Ride

@shared_task
def update_ride_location(ride_id, new_location):
    try:
        ride = Ride.objects.get(id=ride_id)
        # Simulate location update
        # ride.current_location = new_location
        ride.save()
    except Ride.DoesNotExist:
        pass
