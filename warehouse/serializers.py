from rest_framework import serializers
from core.serializers import BaseNodeSerializer, BaseOrderSerializer
from warehouse.models import Order, Store


class StoreSerializer(BaseNodeSerializer):
    class Meta(BaseNodeSerializer.Meta):
        model = Store


class OrderSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta):
        model = Order
        fields = BaseOrderSerializer.Meta.fields  # + ['store_id']

    # store_id = serializers.PrimaryKeyRelatedField(queryset=Store.objects.all(), read_only=True)

    # def create(self, validated_data):
    #     validated_data['store'] = validated_data.pop('store_id')
    #     return super().create(validated_data)
    #
    # def update(self, instance, validated_data):
    #     validated_data['store'] = validated_data.pop('store_id')
    #     return super().update(instance, validated_data)
