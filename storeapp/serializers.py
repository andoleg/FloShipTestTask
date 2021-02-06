from rest_framework import serializers
from core.serializers import BaseOrderSerializer, BaseNodeSerializer
from storeapp.models import Order, Warehouse


class WarehouseSerializer(BaseNodeSerializer):
    class Meta(BaseNodeSerializer.Meta):
        model = Warehouse
        fields = BaseNodeSerializer.Meta.fields + ['active']
    active = serializers.BooleanField()


class OrderSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta):
        model = Order
        fields = BaseOrderSerializer.Meta.fields  # + ['warehouse_id']
    #
    # warehouse_id = serializers.PrimaryKeyRelatedField(queryset=Warehouse.objects.all())
    #
    # def create(self, validated_data):
    #     validated_data['warehouse'] = validated_data.pop('warehouse_id')
    #     return super().create(validated_data)
    #
    # def update(self, instance, validated_data):
    #     validated_data['warehouse'] = validated_data.pop('warehouse_id')
    #     return super().update(instance, validated_data)
