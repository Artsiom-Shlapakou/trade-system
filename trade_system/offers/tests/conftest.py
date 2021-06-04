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
    slot = mixer.blend('items.InventorySlot',
                       item=item,
                       inventory=created.inventory,
                       quantity=20)
    created.inventory.slots.add(slot)
    return created


@pytest.fixture
def buyer(mixer):
    created = mixer.blend('users.User')
    created.wallet.bank = 10000
    created.wallet.save()
    return created


@pytest.fixture
def another_buyer(mixer):
    created = mixer.blend('users.User')
    created.wallet.bank = 10000
    created.wallet.save()
    return created


def offer(mixer, item, seller):
    return mixer.blend('offers.Offer',
                       user=seller,
                       item=item,
                       type=1,
                       expected_price=180,
                       initial_quantity=20,
                       is_active=True)


@pytest.fixture
def another_offer(mixer, another_item, seller):
    return mixer.blend('offers.Offer',
                       user=seller,
                       item=another_item,
                       type=1,
                       is_active=True)


@pytest.fixture
def buyer(mixer):
    return mixer.blend("users.User")


@pytest.fixture
def buy_offer(mixer, item, buyer):
    return mixer.blend('offers.Offer',
                       user=buyer,
                       item=item,
                       type=0,
                       expected_price=300,
                       is_active=True)