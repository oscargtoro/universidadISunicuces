from app.celery_app import app
from datetime import datetime

@app.task
def hello_task():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Hello! Task executed at {current_time}")
    return "Hello task completed"

@app.task
def morning_task():
    print("Good morning! Starting the day's tasks")
    return "Morning task completed"

@app.task
def evening_task():
    print("Good evening! Finishing the day's tasks")
    return "Evening task completed"