import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ScrapperApi.settings')

app = Celery('ScrapperApi')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
