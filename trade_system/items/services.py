from trade_system.items.models import Item, WatchList, Inventory, WatchlistSlot
   
   
def add_items_in_watchlist(user, item_pk):
    item = Item.objects.get(pk=item_pk)
    slot = WatchlistSlot.objects.create(item=item,watchlist=user.watchlist)
    user.watchlist.watchlist_slots.add(slot)


def get_users_watchlist(user):
    return WatchList.objects \
        .prefetch_related('watchlist_slots') \
        .get(user=user)


def get_users_inventory(user):
    return Inventory.objects.prefetch_related('inventory_slots').get(user=user)


def get_all_items():
    return Item.objects \
        .prefetch_related('currency') \
        .prefetch_related('price') \
        .all()