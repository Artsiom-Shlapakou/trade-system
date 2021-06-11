import pytest


pytestmark = [pytest.mark.django_db]


@pytest.fixture
def currency(mixer):
    return mixer.blend('items.Currency')


@pytest.fixture
def offer_item(mixer, currency):
    return mixer.blend('items.Item',
                       name="Alphabet",
                       short_code="GOOG")


@pytest.fixture
def item(mixer, currency):
    return mixer.blend('items.Item',
                       id=1,
                       currency=currency)


@pytest.fixture
def offer(mixer, item, auth_user):
    return mixer.blend('offers.Offer',
                       user=auth_user,
                       item=item,
                       initial_quantity=30,
                       expected_price=100,
                       type=0)


@pytest.fixture
def user(mixer):
    return mixer.blend('users.User')


# @pytest.fixture
# def seller(mixer, offer_item):
#     created = mixer.blend('users.User')
#     slot = mixer.blend('items.Inventory',
#                        item=offer_item,
#                        inventory=created.inventory,
#                        quantity=20)
#     created.inventory.slots.add(slot)
#     return created


@pytest.fixture
def buyer(mixer):
    created = mixer.blend('users.User')
    created.wallet.bank = 10000
    return created