from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from trading.models import NetworkNode
from trading.serializers import TradingSerializer, TradingUpdateSerializer


class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    permission_classes = [IsAuthenticated]

    default_serializer = TradingSerializer
    serializers = {
        'update': TradingUpdateSerializer,
        'partial_update': TradingUpdateSerializer
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)
