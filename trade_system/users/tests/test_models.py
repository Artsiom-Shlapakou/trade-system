from trade_system.conftest import auth_user
import pytest
import decimal
from trade_system.users.models import User, Wallet

pytestmark = pytest.mark.django_db


# def test_user_get_absolute_url(user: User):
#     assert user.get_absolute_url() == f"/users/{user.username}/"


def test_user_creation_signals_work(mixer):
    created = mixer.blend('users.User')

    assert created.wallet
    assert created.watchlist
    assert created.inventory


def test_buyer_wallet_bank(buyer):
    assert buyer.wallet.bank == 10000


# def test_seller_inventory(seller, offer_item):
#     assert seller.inventory.slots
#     assert seller.inventory.slots.get(item=offer_item).quantity == 20


def test_wallet_signal(auth_user, offer):
    auth_user.wallet.balace = 1000
    auth_user.wallet.save()

#     offer.refresh_from_db()
#     assert not offer.is_active


@pytest.mark.parametrize('money', [
    decimal.Decimal('10.31'),
    decimal.Decimal('320.41'),
])
def test_add_money(user, money):
    user.wallet.add_money(money)

    assert user.wallet.balance == money


@pytest.mark.parametrize('money', [
    0,
    decimal.Decimal('-10.12'),
    decimal.Decimal('-240.3445'),
])
def test_user_wallet_deposit_exceptions(user, money):
    with pytest.raises(ValueError):
        user.wallet.add_money(money)