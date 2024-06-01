from django.urls import path, re_path

from hpwd.consumers import Consumer

ws_urlpatterns = [
    path("ws/test/", Consumer.as_asgi()),
    re_path(r"ws/chat/(?P<room_name>\w+)/$", Consumer.as_asgi()),
]