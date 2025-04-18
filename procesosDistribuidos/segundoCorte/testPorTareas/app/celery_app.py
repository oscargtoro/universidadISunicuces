from celery import Celery
from celery.schedules import crontab

app = Celery('tasks',
             broker='redis://redis:6379/0',
             backend='redis://redis:6379/0',
             include=['app.tasks'])

app.conf.beat_schedule = {
    'task-every-morning': {
        'task': 'app.tasks.morning_task',
        'schedule': crontab(hour=20, minute=31)
    },
    'task-every-evening': {
        'task': 'app.tasks.evening_task',
        'schedule': crontab(hour=18, minute=0)
    }
}