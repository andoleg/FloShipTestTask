from rest_framework import viewsets
from rest_framework import mixins

from storeapp.models import Order
from storeapp.serializers import OrderSerializer


class OrderViewSet(mixins.UpdateModelMixin,
                   mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


