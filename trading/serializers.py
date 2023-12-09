from rest_framework import serializers

from trading.models import NetworkNode


class TradingSerializer(serializers.ModelSerializer):
    """Сериализатор объекта сети"""
    class Meta:
        model = NetworkNode
        fields = '__all__'


class TradingUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор объекта сети"""
    class Meta:
        model = NetworkNode
        exclude = ('debt_to_supplier',)
