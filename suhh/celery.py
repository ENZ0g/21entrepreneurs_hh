from celery import Celery
from celery.schedules import crontab
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'suhh.settings')
app = Celery('website')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'clean_db_every_day': {
        'task': 'website.tasks.delete_expired_database_records',
        'schedule': crontab(hour=17, minute=0),
    },
}

app.autodiscover_tasks()
