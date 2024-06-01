from django.urls import path

from . import views
app_name = "hpwd"

urlpatterns = [
    path("test", views.test, name="test"),
    path("home", views.index, name="index"),
    path("pwd/", views.pwd, name="pwd"),
    path("<str:room_name>/", views.room, name="room"),

]