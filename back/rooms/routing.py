from django.urls import re_path
from rooms.consumers import TicTacToeConsumer

websocket_urlpatterns = [
    re_path(r'^ws/$', TicTacToeConsumer.as_asgi()),
]