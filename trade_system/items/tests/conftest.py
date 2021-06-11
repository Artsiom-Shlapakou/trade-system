import pytest
from django.contrib.auth import get_user_model
from trade_system.offers.choises import BUY, SALE


User = get_user_model()

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def user(mixer):
    return mixer.blend('users.User')


@pytest.fixture
def currency(mixer):
    return mixer.blend('items.Currency')


@pytest.fixture
def item(mixer, currency):
    return mixer.blend('items.Item',
                       name="Alphabet",
                       short_code="GOOG",
                       currency=currency)


@pytest.fixture
def another_item(mixer, currency):
    return mixer.blend("items.Item",
                       currency=currency)


@pytest.fixture
def offer(mixer, item, auth_user):
    return mixer.blend('offers.Offer',
                       user=auth_user,
                       item=item,
                       type=BUY)


@pytest.fixture
def another_offer(mixer, item, auth_user):
    return mixer.blend('offers.Offer',
                       user=auth_user,
                       item=item,
                       type=SALE)


@pytest.fixture
def user(mixer, item):
    created = mixer.blend("users.User")
    slot = mixer.blend("items.WatchlistSlot",
                       item=item,
                       watchlist=created.watchlist)
    created.watchlist.watchlist_slots.add(slot)
    inv_slot = mixer.blend("items.InventorySlot",
                           item=item,
                           inventory=created.inventory)
    created.inventory.inventory_slots.add(inv_slot)
    return created