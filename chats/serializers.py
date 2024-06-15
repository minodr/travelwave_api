from rest_framework import serializers

from .models import Chat


class ChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = ["message"]

    def create(self, validated_data):
        sender = validated_data.get("sender")
        receiver = validated_data.get("receiver")

        return Chat.objects.create(
            sender=sender,
            receiver=receiver,
            message=validated_data.get("message"),
            status="sent",
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["sender"] = instance.sender.phone_number
        data["receiver"] = instance.receiver.phone_number
        data["edited"] = instance.edited
        data["status"] = instance.status

        return data
