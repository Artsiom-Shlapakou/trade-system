from trade_system.offers.models import Offer
from trade_system.transactions.models import Trade
from trade_system.offers.choises import BUY, SALE

def search_offer(required_item, required_price):
    offers = Offer.objects.all()
    buyers = [offer for offer in offers if offer.order_type == BUY]
    sellers = [offer for offer in offers if offer.order_type == SALE and offer.is_active]

    for buyer in buyers:
        pass