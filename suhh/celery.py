from celery import Celery
from celery.schedules import crontab
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'suhh.settings')
app = Celery('suhh')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.timezone = 'Europe/Moscow'

app.conf.beat_schedule = {
    'clear_db_daily': {
        'task': 'website.tasks.delete_expired_database_records',
        'schedule': crontab(minute=55, hour=23)
    }
}
