from django.urls import path

from rms.apps.notifications.api.consumers import NotificationConsumer

websocket_urlpatterns = [
    path("ws/notifications/", NotificationConsumer.as_asgi(), name="notifications"),
]
