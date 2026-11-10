from channels.generic.websocket import AsyncJsonWebsocketConsumer


class NotificationConsumer(AsyncJsonWebsocketConsumer):
    """Kênh WebSocket theo user; chưa áp đặt payload nghiệp vụ cụ thể."""

    async def connect(self):
        user = self.scope.get("user")
        if not user or not user.is_authenticated:
            await self.close(code=4401)
            return

        self.group_name = f"user_{user.pk}_notifications"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()
        # Gửi thông báo xác nhận kết nối để client phân biệt trạng thái mở socket.
        await self.send_json({"type": "connection.ready"})

    async def disconnect(self, close_code):
        group_name = getattr(self, "group_name", None)
        if group_name:
            await self.channel_layer.group_discard(group_name, self.channel_name)

    async def rms_event(self, event):
        """Chuyển tiếp event đã được outbox publisher gửi tới đúng user group."""
        await self.send_json(
            {
                "event_id": event["event_id"],
                "type": event["event_type"],
                "payload": event["payload"],
            }
        )
