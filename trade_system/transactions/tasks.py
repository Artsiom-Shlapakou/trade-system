from trade_system.transactions.services import task
from config import celery_app
# from trade_system.transactions.services import search_offer
from trade_system.offers import services

@celery_app.task()
def perform_trade(seller, buyers):
    task(seller, buyers)


@celery_app.task()
def task_search_offer():
    sellers = services.get_opened_sale_offers()
    buyers = services.get_opened_purchase_offers()

    for seller_offer in sellers:
        perform_trade.delay(seller_offer, buyers)