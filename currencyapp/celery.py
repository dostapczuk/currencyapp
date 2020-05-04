import os
from celery import Celery
from celery.schedules import crontab
import logging

logger = logging.getLogger("Celery")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'currencyapp.settings')
app = Celery('currencyapp')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    "fetch_exchange_values": {
        "task": "scraper.tasks.fetch_exchange_values",
        "schedule": crontab(minute=15, hour=8, day_of_week='1-5')
    }
}
