from Inventory.models import ItemType
from Player.models import Player
from GameMap.models import Location
from rest_framework import serializers


class ItemTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ItemType
        fields = ['id', 'name']


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ['url', 'name', 'player_class', 'email', 'level', 'position']


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ['url', 'locationId', 'description', 'locationType']