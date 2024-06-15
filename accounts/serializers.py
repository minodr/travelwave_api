from rest_framework import serializers

from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = [
            "full_name",
            "phone_number",
            "is_driver",
            "driver_license",
            "password",
        ]

    def create(self, validated_data):
        phone_number = validated_data.pop("phone_number")
        password = validated_data.pop("password")
        user = CustomUser.objects.create_user(
            phone_number,
            password,
            **validated_data,
        )
        return user


class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "full_name",
            "phone_number",
            "is_driver",
            "driver_license",
            "rating",
        ]
