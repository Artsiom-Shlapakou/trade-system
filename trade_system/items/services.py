from trade_system.items.models import Item, WatchList, Inventory
   
   
def add_items_in_watchlist(user, item_pk):
    item = Item.objects.get(pk=item_pk)
    watchlist = WatchList.objects.get(user=user)
    watchlist.items.add(item)
    watchlist.save()


def get_users_watchlist(user):
    return WatchList.objects.prefetch_related('items').get(user=user)


def get_users_inventory(user):
    return Inventory.objects.prefetch_related('items').get(user=user)