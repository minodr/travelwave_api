from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import CustomUser

from .models import Chat
from .serializers import ChatSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_inbox(request):
    user = request.user
    inbox_chats = Chat.objects.filter(
        Q(sender=user) | Q(receiver=user)
    ).prefetch_related("sender", "receiver")

    serializer = ChatSerializer(inbox_chats, many=True)

    return Response(
        serializer.data,
        status=status.HTTP_200_OK,
    )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_chat_detail(request, pk):
    chat = Chat.objects.filter(pk=pk).first()

    if chat is None:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ChatSerializer(chat)

    return Response(
        serializer.data,
        status=status.HTTP_200_OK,
    )


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_message(request, pk):
    message = request.data.get("message")

    chat = Chat.objects.filter(pk=pk).first()

    if chat is not None:
        chat.message = message
        chat.edited = True
        chat.save()

        return Response(
            {"message": "Message updated successfully."},
            status=status.HTTP_200_OK,
        )

    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_message(request, pk):
    message = Chat.objects.filter(pk=pk).first()

    if message is not None:
        message.delete()
        return Response(
            {"message": "Message deleted successfully."},
            status=status.HTTP_200_OK,
        )

    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def send_message(request):
    serlializer = ChatSerializer(data=request.data)

    sender_id = request.data.get("sender")
    receiver_id = request.data.get("receiver")

    sender = CustomUser.objects.filter(phone_number=sender_id).first()
    receiver = CustomUser.objects.filter(phone_number=receiver_id).first()

    if not all([sender, receiver]):  # check if sender and receiver exist
        return Response(status=status.HTTP_404_NOT_FOUND)

    if serlializer.is_valid(raise_exception=True):
        serlializer.save(sender=sender, receiver=receiver)

        return Response(
            serlializer.data,
            status=status.HTTP_201_CREATED,
        )

    return Response(
        serlializer.errors,
        status=status.HTTP_400_BAD_REQUEST,
    )
