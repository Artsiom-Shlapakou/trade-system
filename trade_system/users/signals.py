from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from trade_system.users.models import Wallet

User = get_user_model()

@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    
    from trade_system.items.models import Inventory, WatchList
    if created:
        print('qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq')
        Wallet.objects.create(user=instance)
        Inventory.objects.create(user=instance)
        WatchList.objects.create(user=instance)


# @receiver(post_save, sender=User) 
# def save_profile(sender, instance, **kwargs):
#         instance.profile.save()