from __future__ import absolute_import
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')


app = Celery(__name__)
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()

TASK_SERIALIZER = 'json'
ACCEPT_CONTENT = ['json']
