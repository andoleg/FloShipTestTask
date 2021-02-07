import secrets

from django.db import models
from core.enums import OrderStatus


class BaseOrder(models.Model):
    class Meta:
        abstract = True

    # number = models.IntegerField(unique=True)
    number = models.CharField(max_length=6, verbose_name='Order number')
    status = models.CharField(
        max_length=15, choices=OrderStatus.choices, default=OrderStatus.new
    )

    def __str__(self):
        return str(self.number)


class BaseNode(models.Model):
    class Meta:
        abstract = True

    url = models.CharField(max_length=25, verbose_name="URL")
    name = models.CharField(max_length=25)
    server_token = models.CharField(max_length=25, blank=True)
    client_token = models.CharField(max_length=25, blank=True, default="")

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.server_token:
            self.server_token = secrets.token_hex(10)
        return super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.name
