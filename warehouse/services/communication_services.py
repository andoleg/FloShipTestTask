from warehouse.celery import celery_app
from warehouse.serializers import OrderSerializer


class Communication:
    def send_request(self, order, ip_address):
        order = OrderSerializer(instance=order).data

        celery_app.send_task(
            'tasks.send_request',
            retry=True,
            retry_policy={
                'max_retries': 3,
                'interval_start': 3,
                'interval_step': 1,
                'interval_max': 6
            },
            args=[order, ip_address]
        )
