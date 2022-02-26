import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "main_room"

        async_to_sync(self.channel_layer.group_add)(
            self.room_name
        )


        self.accept()
