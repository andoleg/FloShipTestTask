from django.db import models
from core.base_choices import OrderStatus


class BaseOrder(models.Model):
    class Meta:
        abstract = True

    name = models.IntegerField()
    status = models.CharField(max_length=15, choices=OrderStatus.choices, default=OrderStatus.new)

    def __str__(self):
        return str(self.name)


class BaseNode(models.Model):
    class Meta:
        abstract = True

    ip_address = models.CharField(max_length=25, verbose_name='IP address')
    name = models.CharField(max_length=25, verbose_name='Warehouse name')
    token = models.CharField(max_length=25)

    def __str__(self):
        return self.name
