# Platform/celery.py
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Platform.settings')

app = Celery('Platform')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
