from django.contrib import admin
from trade_system.users.models import Wallet
from django.contrib.auth import get_user_model


User = get_user_model()

admin.site.register(User)
admin.site.register(Wallet)
