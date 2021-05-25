from django.db import models
from trade_system.items.models import Item
from trade_system.users.models import User
from trade_system.offers.models import Offer


class Trade(models.Model):
    """Information about a certain transaction"""
    item = models.ForeignKey(Item, blank=True, null=True, on_delete=models.SET_NULL)
    seller = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name = 'seller_trade',
        related_query_name='seller_trade'
    )
    buyer = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name = 'buyer_trade',
        related_query_name='buyer_trade'
    )
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    buyer_offer = models.ForeignKey(
        Offer,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name = 'buyer_trade',
        related_query_name='buyer_trade'
    )
    seller_offer = models.ForeignKey(
        Offer,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name = 'seller_trade',
        related_query_name='seller_trade'
    )