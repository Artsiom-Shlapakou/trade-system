from trade_system.users.models import Wallet
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }

        
class WalletSerializers(serializers.ModelSerializer):

    class Meta:
        model = Wallet

        fields = [
            'money'
        ]