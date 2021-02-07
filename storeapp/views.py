from core.views.order import BaseOrderViewSet
from storeapp.models import Order
from storeapp.serializers import CreateOrderSerializer


class OrderViewSet(BaseOrderViewSet):
    queryset = Order.objects.all()
    serializer_class = CreateOrderSerializer
