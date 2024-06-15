from rest_framework import serializers

from accounts.models import CustomUser

from .models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    driver = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(),
        required=False,
    )

    class Meta:
        model = Vehicle
        fields = [
            "driver",
            "name",
            "make",
            "model",
            "year",
            "color",
            "license_plate",
            "number_of_seats",
        ]
