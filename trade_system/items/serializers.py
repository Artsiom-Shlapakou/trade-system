from rest_framework import serializers
from trade_system.items.models import Currency, Item, Price, WatchList, Inventory
from trade_system.users.serializers import UserSerializers


class CurrencySerializer(serializers.ModelSerializer): 
    
    class Meta:
        model = Currency
        field = [
            'code ',
            'name'
        ]
    

class ItemSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer(read_only=True) 

    class Meta:
        model = Item
        field = [
            'price',
            'currency',
            'details'
        ]


class WatchListSerializer(serializers.ModelSerializer):
    user = UserSerializers
    item = ItemSerializer(many=True)

    class Meta:
        model = WatchList
        field = [
            'user',
            'item'
        ]


class PriceSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer
    item = ItemSerializer(many=True)

    class Meta:
        model = Price
        field = [
            'currency',
            'item',
            'price',
            'date'
        ]
    

class InventorySerializer(serializers.ModelSerializer):
    user = UserSerializers
    item = ItemSerializer(many=True)

    class Meta:
        model = Inventory
        fields = [
            'user',
            'item',
            'quantity'
        ]