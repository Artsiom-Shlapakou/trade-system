from rest_framework import viewsets
from rest_framework import mixins
from trade_system.offers.models import Offer
from trade_system.offers.serializers import OfferSerializers


class OfferListCreateRetriveViewSet(mixins.ListModelMixin,
                                    mixins.CreateModelMixin,
                                    mixins.RetrieveModelMixin,
                                    viewsets.GenericViewSet):
                                
    queryset = Offer.objects.all()
    serializer_class = OfferSerializers