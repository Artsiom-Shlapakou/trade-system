#from django.contrib.auth import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from decimal import Decimal


class Wallet(models.Model):
    money = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True, default=Decimal('0.00'))


class User(AbstractUser):
    """Default user for trade-system."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    wallet = models.OneToOneField(Wallet, on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
