from enum import unique
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.base import Model


User = get_user_model()


class StockBase(models.Model):
    """Base"""
    code = models.CharField(_("Code"), max_length=8, unique=True)
    name = models.CharField(_("Name"), max_length=128, unique=True)

    class Meta:
        abstract = True
    

class Currency(StockBase):
    """Currency"""

    def __str__(self):
        return self.code
    
    class Meta:
        verbose_name = _("Currency")
        verbose_name_plural = _("Currencies")


class Item(StockBase):
    """Perticular stock"""
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    currency = models.ForeignKey(Currency, blank=True, null=True, on_delete=models.SET_NULL)
    details = models.TextField(_("Details"), null=True, max_length=512)

    def __str__(self):
        return self.code


class WatchList(models.Model):
    """Current user, favorite list of stocks"""
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='watchlist')
    item = models.ForeignKey(Item, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.item.code


class Price(models.Model):
    """Item prices"""
    currency = models.ForeignKey(Currency, blank=True, null=True, on_delete=models.SET_NULL)
    item = models.ForeignKey(Item, blank=True, null=True, on_delete=models.CASCADE, related_name=_('prices'),
                            related_query_name=_('prices'))
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    date = models.DateTimeField(unique=True, blank=True, null=True)
    

class Inventory(models.Model):
    """The number of stocks a particular user has"""
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='inventory')
    item = models.ForeignKey(Item, blank=True, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(_("Stocks quantity"), default=0)

    def __str__(self):
        return '{} user {} {} pieces'.format(self.user, self.item, self.quantity)

    def remove_quantity(self, quantity):
        self.quantity -= quantity
        self.save()

    def add_quantity(self, quantity):
        self.quantity += quantity
        self.save()
    
    class Meta:
        verbose_name = _("Inventory")
        verbose_name_plural = _("Inventories")