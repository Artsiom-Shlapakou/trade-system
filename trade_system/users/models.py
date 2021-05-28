#from django.contrib.auth import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from decimal import Decimal


class User(AbstractUser):
    """Default user for trade-system."""

    name = CharField(_("Name of User"), blank=True, max_length=255)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    money = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True, default=Decimal('0.00'))

    def add_money(self, cost):
        """ Add money to wallet"""
        self.balance += cost
        self.save()

    def take_money(self, cost):
        """Take out any money"""
        self.balance -= cost
        self.save()