import pytest
from rest_framework.reverse import reverse
from trade_system.base.tests.mixer import mixer as _mixer
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from trade_system.items.models import Item, Inventory, Currency

User = get_user_model()


@pytest.fixture
def mixer():
    return _mixer


@pytest.fixture
def api():
    return APIClient()


@pytest.fixture
def auth_user(mixer):
    user = User.objects.create_user(
        "testuser123",
        'test@gmail.com',
        "testpasSword123"
    )
    return user


@pytest.fixture
def token(api, auth_user):
    token_url = reverse('token_obtain_pair')
    login_data = {
        "username": "testuser123",
        "password": "testpasSword123"
    }
    token = api.post(token_url,
                     login_data,
                     format="json")

    return token


@pytest.fixture
def creds(api, token):
    api.credentials(HTTP_AUTHORIZATION=f"Bearer {token.data['access']}")