from rest_framework import serializers
from trade_system.users.models import User
from trade_system.users.models import Wallet


class WalletSerializers(serializers.ModelSerializer):

    class Meta:
        model = Wallet

        fields = [
            'money'
        ]


class UserSerializers(serializers.ModelSerializer):
    wallet = WalletSerializers
    
    class Meta:
        model = User

        fields = [
            'name',
            'wallet'
        ]