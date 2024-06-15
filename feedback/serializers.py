from rest_framework import serializers

from accounts.models import CustomUser

from .models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    ride = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(),
        required=False,
    )
    passenger = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(),
        required=False,
    )
    driver = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(),
        required=False,
    )

    class Meta:
        model = Feedback
        fields = [
            "ride",
            "passenger",
            "driver",
            "rating",
            "feedback",
        ]
