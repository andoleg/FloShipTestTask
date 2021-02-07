from rest_framework import serializers
from core.serializers import BaseOrderSerializer
from core.serializers.base import BaseCreateOrderSerializer
from storeapp.models import Order, Warehouse


class OrderSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta):
        model = Order

    token = serializers.ReadOnlyField(source="warehouse.client_token")


class CreateOrderSerializer(BaseCreateOrderSerializer):
    class Meta(BaseCreateOrderSerializer.Meta):
        model = Order

    def validate_token(self, token):
        if not Warehouse.objects.filter(server_token=token).exists():
            raise serializers.ValidationError("Invalid token")
        return token

    def create(self, validated_data):
        token = validated_data.pop("token")
        validated_data["warehouse"] = Warehouse.objects.get(server_token=token)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        token = validated_data.pop("token")
        return super().update(instance, validated_data)
