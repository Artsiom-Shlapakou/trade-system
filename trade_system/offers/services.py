from trade_system.offers.models import Offer
from trade_system.offers.choises import BUY, SALE


def _get_active_offers():
    return Offer.objects.filter(is_active=True)


def get_opened_purchase_offers():
    return _get_active_offers().filter(order_type=BUY).order_by('price')


def get_opened_sale_offers():
    return _get_active_offers().filter(order_type=SALE).order_by('price')


def _get_users_offers(self):
    return Offer.objects.filter(user=self.request.user).filter(is_active=True)


def get_users_purchase_offers():
    return _get_users_offers().filter(order_type=BUY)


def get_users_sale_offers():
    return _get_users_offers().filter(order_type=SALE)