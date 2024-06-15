from rest_framework import serializers

from .models import Ride, RideHistory


class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = [
            "vehicle",
            "status",
            "number_of_passengers",
            "current_location",
            "created_at",
            "updated_at",
        ]


class RideHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RideHistory
        fields = [
            "passenger",
            "ride",
            "pickup_location",
            "drop_location",
            "created_at",
            "updated_at",
        ]
