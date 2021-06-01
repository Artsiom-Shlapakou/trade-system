from django.db import transaction
from trade_system.offers.models import Offer
from trade_system.transactions.models import Trade
from trade_system.offers.choises import BUY, SALE
from trade_system.offers.services import get_opened_sale_offers, get_opened_purchase_offers


def search_offer():
    pass
    # buyers = 
    # sellers = 
    
    # for buyer in buyers:
    #     for seller in sellers:
    #         if buyer.item == seller.item and buyer.price >= seller.price:
    #             Trade.objects.create(item=buyer.item,
    #                             seller=seller.user,
    #                             buyer=buyer.user,
    #                             quantity=min(buyer.quantity, seller.quantity),
    #                             unit_price=calculate_trade_amount(buyer, seller),
    #                             buyer_offer=buyer,
    #                             seller_offer=seller
    #                             )
    #             save_trade(buyer, seller)

# @transaction.atomic
# def save_trade(buyer, seller):
#     cost = calculate_trade_amount(buyer, seller)
#     buyer.add_quantity()
#     buyer.take_money(cost)
#     seller.remove_quantity()
#     seller.add_money(cost)
#     buyer.save()
#     seller.save()

def calculate_trade_amount(buyer, seller):
    """Calculation of the total transaction amount"""
    return seller.price * min(buyer.quantity, seller.quantity)