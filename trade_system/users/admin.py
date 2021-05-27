from django.contrib import admin
from trade_system.users.models import User, Wallet
# from django.contrib.auth import get_user_model


# User = get_user_model()

admin.site.register(User)
admin.site.register(Wallet)
# @admin.register(User)
# class UserAdmin(auth_admin.UserAdmin):
#     pass