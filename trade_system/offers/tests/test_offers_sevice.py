import pytest
from trade_system.offers import services

pytestmark = [pytest.mark.django_db]


def test_get_all_active_sell_offers_service_queries_num(django_assert_num_queries,
                                                        offer,
                                                        another_offer):
    with django_assert_num_queries(3):
        data = services.get_opened_sale_offers()
        print(data[0].item.name)
        print(data[1].user.wallet)
        print(data[1].user.inventory)


def test_get_suitable_offers_queries_num(django_assert_num_queries, offer, buy_offer):
    with django_assert_num_queries(5):
        data = services.get_opened_purchase_offers(offer)

        print(data[0].item.name)
        print(data[0].user.wallet)
        print(data[0].user.inventory)

        assert data[0].is_active
        assert data[0].expected_price == 300