from trade_system.users.models import Wallet


def add_money(instance, cost):
    """ Add money to wallet"""
    seller_balance = Wallet.objects.get(user=instance.user.id)
    seller_balance.balance += cost
    seller_balance.save()


def take_money(instance, cost):
    """Take out any money"""
    buyer_balance = Wallet.objects.get(user=instance.user.id)
    buyer_balance.balance -= cost
    buyer_balance.save()