#from django.contrib.auth import models
# from trade_system.users.signals import create_user
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.db.models.signals import post_save
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from decimal import Decimal
from django.core.exceptions import ValidationError


def validate_money(money):
    if money <= 0:
        raise ValidationError("")
    return money


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
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wallet')
    balance = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True, default=Decimal('0.00'))
    
    def __str__(self):
        return '{} {}'.format(self.user, self.balance)

    def add_money(self, money):
        """ Add money to wallet"""
        try:
            money = validate_money(money)
            self.balance += money
            self.save()
        except ValidationError:
            raise ValueError("Provided amount of money was incorrect!")


    def take_money(self, money):
        """Take out any money"""
        try:
            money = validate_money(money)
            self.balance -= money
            self.save()
        except ValidationError:
            raise ValueError("Provided amount of money was incorrect!")

    



# post_save.connect(create_user, sender=User)