import json

from channels.generic.websocket import AsyncWebsocketConsumer

from .models import Chat


class ChatConsumer(AsyncWebsocketConsumer):
    def connect(self):
        self.root_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.root_name}"

        self.accept()

    def disconnect(self, code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        sender_id = text_data_json["sender_id"]
        receiver_id = text_data_json["receiver_id"]
        message = text_data_json["message"]

        Chat.objects.create(sender=sender_id, receiver=receiver_id, message=message)

        self.send_chat_message(sender_id, receiver_id, message)

    def send_chat_message(self, sender_id, receiver_id, message):
        self.send(
            text_data=json.dumps(
                {
                    "sender_id": sender_id,
                    "receiver_id": receiver_id,
                    "message": message,
                },
            )
        )
