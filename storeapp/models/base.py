from core.models import BaseOrder, BaseNode
from django.db import models


class Order(BaseOrder):
    warehouse = models.ForeignKey("Warehouse", on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class Warehouse(BaseNode):
    class Meta:
        verbose_name = "Warehouse"
        verbose_name_plural = "Warehouses"
