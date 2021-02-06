import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storeapp.settings')
celery_app = Celery('storeapp', broker='amqp://guest:guest@localhost:5672//')
# celery_app.config_from_object('django.conf:settings', namespace='CELERY')
# celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
#
#
# def send_request_to_broker(instance):
#     order = OrderSerializer(instance=instance).data
#     celery_app.send_task(
#         'tasks.send_request',
#         retry=True,
#         retry_policy={
#             'max_retries': 3,
#             'interval_start': 3,
#             'interval_step': 1,
#             'interval_max': 6
#         },
#         kwargs=order,
#     )
