from rest_framework import generics, viewsets

from trading.models import NetworkNode
from trading.serializers import TradingSerializer, TradingUpdateSerializer


class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()

    default_serializer = TradingSerializer
    serializers = {
        'update': TradingUpdateSerializer,
        'partial_update': TradingUpdateSerializer
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)
