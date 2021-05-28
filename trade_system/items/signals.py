from django.dispatch import receiver
from django.db.models.signals import post_save
from trade_system.users.models import User, Wallet
from trade_system.items.models import WatchList, Inventory, 


@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if created:
        instance.wallet = Wallet.objects.create(user=instance)
        Inventory.objects.create(user=instance)
        WatchList.objects.create(user=instance)