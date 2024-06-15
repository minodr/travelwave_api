from django.db import models

from accounts.models import CustomUser

STATUS_CHOICES = [
    ("sent", "Sent"),
    ("received", "Received"),
    ("read", "Read"),
    ("deleted", "Deleted"),
    ("pending", "Pending"),
]


class Chat(models.Model):
    sender = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="message_sent",
    )
    receiver = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="message_received",
    )

    message = models.TextField()
    edited = models.BooleanField(default=False)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="pending",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk)
