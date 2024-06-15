from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def available_rides(request):
    return Response()


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def pick_ride(request):
    return Response()


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_ride(request):
    return Response()


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def update_ride_detail(request):
    return Response()


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def cancel_ride(request):
    return Response()


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_passenger(request):
    return Response()


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def remove_passenger(request):
    return Response()


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_ride_passengers(request):
    return Response()


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_ride_detail(request):
    return Response()


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_ride_location(request):
    return Response()


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def get_nearby_passengers(request):
    return Response()


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_passenger_location(request):
    return Response()
