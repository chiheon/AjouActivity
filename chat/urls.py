# chat/urls.py
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.chat, name='chat'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
    #path('chat/<str:room_name>/', room, name='room'),
]