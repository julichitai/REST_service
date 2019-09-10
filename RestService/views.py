from django.shortcuts import render
from Inventory.models import ItemType
from Player.models import Player
from GameMap.models import Location
from rest_framework import viewsets
from RestService.serializers import PlayerSerializer, LocationSerializer, ItemTypeSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class ItemTypeList(viewsets.ModelViewSet):
    queryset = ItemType.objects.all()
    serializer_class = ItemTypeSerializer

