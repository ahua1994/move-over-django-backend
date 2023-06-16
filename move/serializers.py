from rest_framework import serializers
from .models import *


class ItemSerializer(serializers.Serializer):
    class Meta:
        model = Item
        fields = "__all__"


class PlaceSerializer(serializers.Serializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = Place
        fields = "__all__"


class MoveSerializer(serializers.Serializer):
    owner = serializers.StringRelatedField()
    owner_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    places = PlaceSerializer(many=True)
    items = ItemSerializer(many=True)

    class Meta:
        model = Move
        fields = "__all__"
