from trade_system.offers.choises import BUY, SALE
import pytest

pytestmark = [pytest.mark.django_db]


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
    return mixer.blend('items.Item',
                       currency=currency)


@pytest.fixture
def seller(mixer, item):
    created = mixer.blend('users.User')
    slot = mixer.blend('items.Inventory',
                       item=item,
                       inventory=created.inventory,
                       quantity=5)
    created.inventory.inventory_slots.add(slot)
    return created


@pytest.fixture
def buyer(mixer):
    created = mixer.blend('users.User')
    created.wallet.balance = 10000
    created.wallet.save()
    return created


@pytest.fixture
def another_buyer(mixer):
    created = mixer.blend('users.User')
    created.wallet.balance = 1000
    created.wallet.save()
    return created


@pytest.fixture
def offer(mixer, item, seller):
    return mixer.blend('offers.Offer',
                       user=seller,
                       item=item,
                       order_type=BUY,
                       price=100,
                       quantity=20,
                       is_active=True)


@pytest.fixture
def another_offer(mixer, another_item, seller):
    return mixer.blend('offers.Offer',
                       user=seller,
                       item=another_item,
                       order_type=SALE,
                       is_active=True)


@pytest.fixture
def buyer(mixer):
    return mixer.blend("users.User")


@pytest.fixture
def buy_offer(mixer, item, buyer):
    return mixer.blend('offers.Offer',
                       user=buyer,
                       item=item,
                       order_type=BUY,
                       price=100,
                       is_active=True)