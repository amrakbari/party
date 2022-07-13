from django.urls import path
from .views import RoomCreateView


urlpatterns = [
    path('room/', RoomCreateView.as_view()),
]