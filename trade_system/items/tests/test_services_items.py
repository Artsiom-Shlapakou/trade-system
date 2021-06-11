import pytest
from trade_system.items import services

pytestmark = [pytest.mark.django_db]



def test_get_user_watchlist_service(user, item):
    watchlist = services.get_users_watchlist(user)

    assert watchlist.watchlist_slots.first().item.name == item.name


def test_get_user_inventory_service(user, item):
    inventory = services.get_users_inventory(user)

    assert inventory.inventory_slots.first().item.name == item.name