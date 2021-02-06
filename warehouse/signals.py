from django.db.models.signals import post_save
from django.dispatch import receiver

from warehouse.models import Order
from warehouse.services.communication_services import Communication


@receiver(post_save, sender=Order)
def send_on_save(sender, instance, **kwargs):
    Communication().send_request(instance, instance.warehouse.ip_address)

