from django.db import models
from trade_system.users.models import User
from trade_system.items.models import Item
from trade_system.offers.choises import OrderType


class Offer(models.Model):
    """Request to buy or sell specific stocks"""
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    item = models.ForeignKey(Item, blank=True, null=True, on_delete=models.SET_NULL)
    entry_quantity = models.IntegerField('Requested quantity')
    quantity = models.IntegerField('Current quantity')
    order_type = models.PositiveSmallIntegerField(choices=OrderType)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    is_active = models.BooleanField(default=True)