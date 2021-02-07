import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "storeapp.settings")
celery_app = Celery("storeapp")
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
