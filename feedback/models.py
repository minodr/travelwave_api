from django.db import models

from accounts.models import CustomUser
from rides.models import Ride


class Feedback(models.Model):
    ride = models.ForeignKey(
        Ride,
        on_delete=models.CASCADE,
    )
    passenger = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="rider_feedbacks",
    )
    driver = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="passenger_feedbacks",
    )
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    feedback = models.TextField()

    def __str__(self):
        return str(self.pk)
