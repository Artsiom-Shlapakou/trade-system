from config import celery_app
from trade_system.transactions.services import search_offer


@celery_app.task()
def task_search_offer():
    search_offer()