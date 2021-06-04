from django.db import transaction
from trade_system.offers.models import Offer
from trade_system.transactions.models import Trade
from trade_system.offers.choises import BUY, SALE
from trade_system.offers import services


def check_conditions(seller, buyer):
    return bool(buyer.quantity <= seller.quantity and buyer.price >= seller.price and buyer.item == seller.item)


@transaction.atomic
def task(seller, buyers):
    suitable_offers = [buyer for buyer in buyers if check_conditions(seller, buyer)][::-1]
    if suitable_offers:
        offer = suitable_offers.pop()
        if seller.quantity == 0:
            seller.is_active = False
            seller.save()
        Trade.objects.create(item=offer.item,
                        seller=seller.user,
                        buyer=offer.user,
                        quantity=min(offer.quantity, seller.quantity),
                        unit_price=calculate_trade_amount(offer, seller),
                        buyer_offer=offer,
                        seller_offer=seller
                        )
        save_trade(offer, seller)


def search_offer():
    sellers = services.get_opened_sale_offers()
    buyers = services.get_opened_purchase_offers()

    for seller_offer in sellers:
        task.delay(seller_offer, buyers)


@transaction.atomic
def save_trade(buyer, seller):
    cost = calculate_trade_amount(buyer, seller)
    buyer.add_quantity(seller.quantity)
    buyer.take_money(cost)
    seller.remove_quantity(buyer.quantity)
    seller.add_money(cost)
    buyer.save()
    seller.save()


def calculate_trade_amount(buyer, seller):
    """Calculation of the total transaction amount"""
    return seller.price * min(buyer.quantity, seller.quantity)