from storeapp.celery import celery_app
from storeapp.serializers import OrderSerializer


class Communication:
    def send_request(self, order, ip_address):
        order = OrderSerializer(instance=order).data
        celery_app.send_task(
            'core.tasks.send_create_request',
            retry=True,
            retry_policy={
                'max_retries': 0,
                'interval_start': 3,
                'interval_step': 1,
                'interval_max': 6
            },
            args=[order, ip_address]
        )

    def send_update_request(self, order, ip_address):
        order_id = order.id
        order = OrderSerializer(instance=order, fields=['name', 'status']).data
        celery_app.send_task(
            'core.tasks.send_update_request',
            retry=True,
            retry_policy={
                'max_retries': 3,
                'interval_start': 3,
                'interval_step': 1,
                'interval_max': 6
            },
            args=[order, order_id, ip_address]
        )
