from rest_framework import serializers
from .models import *


class MoveSerializer(serializers.Serializer):
    owner = serializers.StringRelatedField()
    owner_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Move
        fields = "__all__"


class ItemSerializer(serializers.Serializer):
    class Meta:
        model = Item
        fields = "__all__"


class PlaceSerializer(serializers.Serializer):
    class Meta:
        model = Place
        fields = "__all__"
