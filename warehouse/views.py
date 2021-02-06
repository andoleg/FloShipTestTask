from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin
from warehouse.models import Order, Store
from warehouse.serializers import OrderSerializer


class OrderViewSet(CreateModelMixin,
                   UpdateModelMixin,
                   viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


