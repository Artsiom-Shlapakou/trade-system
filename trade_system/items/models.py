from enum import unique
from django.db import models
from django.db.models.base import Model
from trade_system.users.models import User


class StockBase(models.Model):
    """Base"""
    code = models.CharField("Code", max_length=8, unique=True)
    name = models.CharField("Name", max_length=128, unique=True)

    class Meta:
        abstract = True
    

class Currency(StockBase):
    """Currency"""

    def __str__(self):
        return self.code
    
    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"


class Item(StockBase):
    """Perticular stock"""
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    currency = models.ForeignKey(Currency, blank=True, null=True, on_delete=models.SET_NULL)
    details = models.TextField("Details", null=True, max_length=512)


class WatchList(models.Model):
    """Current user, favorite list of stocks"""
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    item = models.ForeignKey(Item, blank=True, null=True, on_delete=models.SET_NULL)


class Price(models.Model):
    """Item prices"""
    currency = models.ForeignKey(Currency, blank=True, null=True, on_delete=models.SET_NULL)
    item = models.ForeignKey(Item, blank=True, null=True, on_delete=models.CASCADE, related_name='prices',
                            related_query_name='prices')
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    date = models.DateTimeField(unique=True, blank=True, null=True)
    

class Inventory(models.Model):
    """The number of stocks a particular user has"""
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    item = models.ForeignKey(Item, blank=True, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField("Stocks quantity", default=0)