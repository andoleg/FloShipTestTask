from core.models import BaseOrder, BaseNode
from django.db import models


class Order(BaseOrder):
    warehouse = models.ForeignKey('Warehouse', on_delete=models.PROTECT)


class Warehouse(BaseNode):
    active = models.BooleanField(default=False)


