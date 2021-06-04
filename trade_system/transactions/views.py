from rest_framework.viewsets import ReadOnlyModelViewSet
from trade_system.transactions.models import Trade
from trade_system.transactions.serializers import TradeSerializer


class TradeReadOnlyViewSet(ReadOnlyModelViewSet):
    serializer_class = TradeSerializer

    def get_queryset(self):
        return Trade.objects.filter(user=self.request.user)