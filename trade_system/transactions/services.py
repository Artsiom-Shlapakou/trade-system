from trade_system.users.services import add_money, take_money
from trade_system.offers.models import Offer
from trade_system.transactions.models import Trade
from trade_system.offers.choises import BUY, SALE



def search_offer():
    offers = Offer.objects.filter(is_active=True)
    buyers = [offer for offer in offers if offer.order_type == BUY]
    sellers = [offer for offer in offers if offer.order_type == SALE]

    for buyer in buyers:
        for seller in sellers:
            if buyer.item == seller.item and buyer.price >= seller.price:
                cost = total_trade_amount(buyer, seller)
                Trade.objects.create(item=buyer.item,
                                seller=seller.user,
                                buyer=buyer.user,
                                quantity=min(buyer.quantity, seller.quantity),
                                unit_price=cost,
                                buyer_offer=buyer,
                                seller_offer=seller
                                )
                buyer.add_quantity()
                take_money(buyer, cost)
                seller.reduce_quantity()
                add_money(seller, cost)
                buyer.save()
                seller.save()

def total_trade_amount(buyer, seller):
    """Calculation of the total transaction amount"""
    # current_transaction = Trade.objects.get()
    return seller.price * min(buyer.quantity, seller.quantity)

