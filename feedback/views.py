from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import FeedbackSerializer


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def rate(request):
    serializer = FeedbackSerializer(request.data)

    reviewer = request.data.get("reviewer")
    reviewee = request.data.get("reviewee")
    ride = request.data.get("ride")

    if serializer.is_valid(raise_exception=True):
        serializer.save(
            reviewer=reviewer,
            reviewee=reviewee,
            ride=ride,
        )
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST,
    )
