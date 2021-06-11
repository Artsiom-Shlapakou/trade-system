from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from trade_system.items.models import Item, WatchList, Inventory
from trade_system.items.serializers import (InventorySerializer, ItemSerializer, 
                                            WatchListSerializer, InventorySerializer)

class ItemListRetrieveViewSet(mixins.ListModelMixin, 
                           mixins.RetrieveModelMixin, 
                           viewsets.GenericViewSet):
    
    queryset = Item.objects.all()
    serializer_class = ItemSerializer



class WatchlistRetrieveUpdateViewSet(mixins.ListModelMixin,
                                     mixins.RetrieveModelMixin,
                                     mixins.UpdateModelMixin,
                                     viewsets.GenericViewSet):

    serializer_class = WatchListSerializer
    
    def get_queryset(self):
        return WatchList.objects.select_related('user') \
            .select_related("item") \
            .filter(user=self.request.user)

    @action(methods=['POST'], detail=True)
    def add_to_watchlist(self, request, pk=None):
        pass


class InventoryListRetrieveViewSet(mixins.RetrieveModelMixin, 
                                   mixins.ListModelMixin, 
                                   viewsets.GenericViewSet):

    serializer_class = InventorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Inventory.objects.filter(user=self.request.user)