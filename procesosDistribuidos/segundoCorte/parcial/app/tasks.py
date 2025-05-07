from celery import Celery
from datetime import datetime

app = Celery('tasks', broker='redis://redis:6379/0',
             backend='redis://redis:6379/0',)

@app.task
def hello_task():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Hello! Task executed at {current_time}")
    return "Hello task completed"
