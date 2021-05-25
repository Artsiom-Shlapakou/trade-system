from django.dispatch import receiver
from django.db.models.signals import post_save
from trade_system.users import User, Wallet


@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(user=instance)