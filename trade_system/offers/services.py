from trade_system.offers.models import Offer
from trade_system.offers.choises import BUY, SALE


def get_active_offers(self):
    return Offer.objects.filter(is_active=True)

def get_opened_purchase_offers(self):
    return get_active_offers().filter(order_type=BUY).order_by(price)

def get_opened_sale_offers(self):
    return get_active_offers().filter(order_type=SALE).order_by(price)
