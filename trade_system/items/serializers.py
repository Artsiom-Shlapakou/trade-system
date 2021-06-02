from rest_framework import serializers
from trade_system.items.models import Currency, Item, Price, WatchList, Inventory
from trade_system.users.serializers import UserSerializers


class CurrencySerializer(serializers.ModelSerializer): 
    
    class Meta:
        model = Currency
        fields = '__all__'
    

class ItemSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer(read_only=True) 

    class Meta:
        model = Item
        fields = '__all__'
        # field = [
        #     'price',
        #     'currency',
        #     'details'
        # ]


class WatchListSerializer(serializers.ModelSerializer):
    user = UserSerializers
    item = ItemSerializer(many=True)

    class Meta:
        model = WatchList
        fields = '__all__'


class PriceSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer
    item = ItemSerializer(many=True)

    class Meta:
        model = Price
        fields = '__all__'
    

class InventorySerializer(serializers.ModelSerializer):
    user = UserSerializers
    item = ItemSerializer(many=True)

    class Meta:
        model = Inventory
        fields = '__all__'