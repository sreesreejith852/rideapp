from geopy.distance import great_circle
from .models import Ride

def find_best_driver(ride):
    available_drivers = User.objects.filter(is_driver=True).exclude(id=ride.rider.id)
    best_driver = None
    min_distance = float('inf')

    for driver in available_drivers:
        driver_location = (driver.latitude, driver.longitude)
        ride_location = (ride.pickup_location_lat, ride.pickup_location_lon)
        distance = great_circle(driver_location, ride_location).km
        if distance < min_distance:
            min_distance = distance
            best_driver = driver

    return best_driver
