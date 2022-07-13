from rest_framework import generics
from .models import Room
from .serializers import RoomSerializers


class RoomCreateView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers
