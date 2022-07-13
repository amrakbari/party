from rest_framework import serializers
from .models import Room


class RoomSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    host = serializers.CharField(required=True)
    guest_can_pause = serializers.BooleanField(required=True)
    votes_to_skip = serializers.IntegerField(required=True)
    code = serializers.CharField(read_only=True)

    class Meta:
        model = Room
        fields = ('id', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at', 'code')
