from core.views.order import BaseOrderViewSet
from warehouse.models import Order
from warehouse.serializers import CreateOrderSerializer


class OrderViewSet(BaseOrderViewSet):
    queryset = Order.objects.all()
    serializer_class = CreateOrderSerializer
