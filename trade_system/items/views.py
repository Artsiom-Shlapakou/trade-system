from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from trade_system.items.models import Item, WatchList
from trade_system.items.serializers import (ItemSerializer, WatchListSerializer
                                            )


class ItemViewSet(viewsets.ModelViewSet):
    
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class WatchlistRetrieveUpdate(  mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                viewsets.GenericViewSet):

    serializer_class = WatchListSerializer
    
    def get_queryset(self):
        return WatchList.objects.filter(user=self.kwargs['user'])