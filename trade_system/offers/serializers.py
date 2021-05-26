from trade_system.users.serializers import UserSerializers
from rest_framework import serializers
from trade_system.offers.models import Offer
from trade_system.items.serializers import ItemSerializer

class OfferSerializers(serializers.ModelSerializer):
    user = UserSerializers
    item = ItemSerializer(many=True)

    class Meta:
        model = Offer
        fields = [
            'user', 
            'item',
            'entry_quantity',
            'quantity',
            'order_type',
            'price',
            'is_active'
        ]