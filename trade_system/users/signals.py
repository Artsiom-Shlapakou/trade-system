from django.dispatch import receiver
from django.db.models.signals import post_save
from trade_system.users.models import Wallet
from trade_system.items.models import Inventory, WatchList
from django.contrib.auth import get_user_model


User = get_user_model()

@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(user=instance)
        Inventory.objects.create(user=instance)
        WatchList.objects.create(user=instance)
        instance.save()