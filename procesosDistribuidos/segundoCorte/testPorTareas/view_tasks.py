from app.celery_app import app

def view_scheduled_tasks():
    print("\nCurrent Scheduled Tasks")
    print("======================")
    
    for task_name, task_info in app.conf.beat_schedule.items():
        print(f"\nTask Name: {task_name}")
        print(f"Task Path: {task_info['task']}")
        print(f"Schedule: {task_info['schedule']}")
        print("-" * 50)

if __name__ == "__main__":
    view_scheduled_tasks()