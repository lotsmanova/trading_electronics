from rest_framework.routers import DefaultRouter
from trading.apps import TradingConfig
from trading.views import NetworkNodeViewSet

app_name = TradingConfig.name
router = DefaultRouter()
router.register(r'trading', NetworkNodeViewSet, basename='trading')

urlpatterns = router.urls
