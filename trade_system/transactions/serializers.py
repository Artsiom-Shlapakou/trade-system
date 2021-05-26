from rest_framework import serializers
from trade_system.offers.serializers import OfferSerializers
from trade_system.users.serializers import UserSerializers
from trade_system.items.serializers import ItemSerializer
from trade_system.transactions.models import Trade


class TradeSerializer(serializers.ModelSerializer):
    item = ItemSerializer(many=True)
    seller = UserSerializers
    buyer = UserSerializers
    buyer_offer = OfferSerializers
    seller_offer = OfferSerializers

    class Meta:

       model = Trade
       fields = [
            'item',
            'seller',
            'buyer'
            'quantity',
            'unit_price',
            'description',
            'buyer_offer',
            'seller_offer'
       ]