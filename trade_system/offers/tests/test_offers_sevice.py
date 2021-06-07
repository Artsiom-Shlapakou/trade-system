import pytest
from trade_system.offers import services

pytestmark = [pytest.mark.django_db]


def test_get_all_active_sell_offers_service_queries_num(offer,  another_offer):
    data = services.get_opened_sale_offers()
    print(data[0].item.name)
    print(data[0].user.wallet)
    print(data[0].user.inventory)


def test_get_suitable_offers_queries_num(offer, buy_offer):
    data = services.get_opened_purchase_offers()
    print(data[0].item.name)
    print(data[0].user.wallet)
    print(data[0].user.inventory)

    assert data[0].is_active
    assert data[0].price == 100