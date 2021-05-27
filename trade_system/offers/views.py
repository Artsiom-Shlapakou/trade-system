from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from trade_system.offers.models import Offer
from trade_system.offers.serializers import OfferSerializers


class OfferListCreateRetriveViewSet(mixins.ListModelMixin,
                                    mixins.CreateModelMixin,
                                    mixins.RetrieveModelMixin,
                                    viewsets.GenericViewSet):
                                
    serializer_class = OfferSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Offer.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)