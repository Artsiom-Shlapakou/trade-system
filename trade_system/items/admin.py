from django.contrib import admin
from trade_system.items.models import Item, Currency, Inventory, WatchList


admin.site.register(Item)
admin.site.register(Currency)
admin.site.register(Inventory)
admin.site.register(WatchList)