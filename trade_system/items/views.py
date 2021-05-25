from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from trade_system.items.models import Item
from trade_system.items.serializers import ItemSerializer


class ItemViewSet(ModelViewSet):
    
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

