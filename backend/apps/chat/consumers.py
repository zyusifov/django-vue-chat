from email import message
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "main_room"
        self.room_group_name = "chat_{}".format(self.room_name)

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.room_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.room_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': "chat_message",
                "message": message
            }
        )

    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'event': 'send',
            'message': message
        }))
