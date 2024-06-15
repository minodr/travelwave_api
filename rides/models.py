from django.db import models

from accounts.models import CustomUser
from vehicles.models import Vehicle

STATUS_CHOICES = [
    ("ongoing", "Ongoing"),
    ("completed", "Completed"),
    ("cancelled", "Cancelled"),
]


class Ride(models.Model):
    class Meta:
        verbose_name = "Ride"
        verbose_name_plural = "Rides"

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
    )

    number_of_passengers = models.IntegerField(default=0)
    current_location = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def available_seats(self):
        return self.vehicle.number_of_seats - self.number_of_passengers - 1


class RideHistory(models.Model):
    class Meta:
        verbose_name = "Ride History"
        verbose_name_plural = "Ride History"

    passenger = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="rides_as_passenger",
    )

    ride = models.ForeignKey(
        Ride,
        on_delete=models.CASCADE,
        related_name="passengers",
    )

    pickup_location = models.CharField(max_length=255)
    drop_location = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    fare_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.0,
    )
