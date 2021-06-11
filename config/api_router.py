from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from trade_system.users.api.views import UserViewSet
from trade_system.offers.views import OfferListCreateRetriveViewSet
from trade_system.items.views import (ItemListRetrieveViewSet, 
                                      InventoryListRetrieveViewSet,
                                      WatchlistRetrieveUpdateViewSet)
                                      

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register(r'offers', OfferListCreateRetriveViewSet, basename='offer')
router.register(r'items', ItemListRetrieveViewSet, basename='items')
router.register(r'inventory', InventoryListRetrieveViewSet, basename='inventory')
router.register(r'watchlist', WatchlistRetrieveUpdateViewSet, basename='watchlist')

app_name = "api"
urlpatterns = router.urls
