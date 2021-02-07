from core.models import BaseOrder
from core.models import BaseNode
from django.db import models


class Order(BaseOrder):
    class Meta(BaseOrder.Meta):
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    store = models.ForeignKey("Store", on_delete=models.PROTECT)


class Store(BaseNode):
    class Meta(BaseNode.Meta):
        verbose_name = "Store"
        verbose_name_plural = "Stores"
