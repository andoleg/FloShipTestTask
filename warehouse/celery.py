import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse.settings')
celery_app = Celery('warehouse', broker='amqp://guest:guest@localhost:5672//')
