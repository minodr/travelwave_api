from django.db import models

from accounts.models import CustomUser


class Vehicle(models.Model):
    driver = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="vehicle",
    )

    name = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(default=2010)
    color = models.CharField(max_length=100)

    license_plate = models.CharField(max_length=10, unique=True)
    number_of_seats = models.PositiveIntegerField(default=4)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_busy = models.BooleanField(default=False)

    def __str__(self):
        return str(self.license_plate)
