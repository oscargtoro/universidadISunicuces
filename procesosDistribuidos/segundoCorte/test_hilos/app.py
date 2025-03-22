import threading
import time
from queue import Queue

class WorkerThread:
    def __init__(self):
        self.queue = Queue()
        self.workers = []
        self.num_threads = 3

    def worker(self, worker_id):
        while True:
            task = self.queue.get()
            if task is None:
                print(f"Worker {worker_id} shutting down...")
                break
            
            print(f"Worker {worker_id} processing task: {task}")
            time.sleep(2)  # Simulate work
            print(f"Worker {worker_id} completed task: {task}")
            self.queue.task_done()

    def start_workers(self):
        for i in range(self.num_threads):
            t = threading.Thread(target=self.worker, args=(i,))
            t.start()
            self.workers.append(t)

    def add_task(self, task):
        self.queue.put(task)

    def stop_workers(self):
        for _ in range(self.num_threads):
            self.queue.put(None)
        for worker in self.workers:
            worker.join()

if __name__ == "__main__":
    worker_system = WorkerThread()
    worker_system.start_workers()

    # Add some example tasks
    for i in range(10):
        worker_system.add_task(f"Task {i}")

    # Wait for all tasks to complete
    worker_system.queue.join()
    worker_system.stop_workers()