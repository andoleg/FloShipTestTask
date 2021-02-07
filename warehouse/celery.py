import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "warehouse.settings")
celery_app = Celery("warehouse")
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
