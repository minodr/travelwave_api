from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import CustomUser

from .serializers import VehicleSerializer


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def vehicle_register(request):
    driver_id = request.data.get("driver_id")

    driver = CustomUser.objects.filter(phone_number=driver_id).first()
    if driver is None:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = VehicleSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save(driver=driver)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST,
    )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def update_vehicle_detail(request):
    driver_id = request.data.get("driver_id")

    driver = CustomUser.objects.filter(phone_number=driver_id).first()
    if driver is None:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = VehicleSerializer(driver.vehicle, data=request.data, partial=True)

    if serializer.is_valid(raise_exception=True):
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST,
    )
