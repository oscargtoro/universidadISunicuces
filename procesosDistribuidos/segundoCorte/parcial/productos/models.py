from django.db import models
from queue import Queue
import time
import threading

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
class Restaurant:
        def __init__(self):
            self.queue = Queue()
            self.chefs = []
            self.num_chefs = 3
            self.output = {}

        def chef_worker(self, chef_id):
            # TODO: Implement chef behavior
            # - Get orders from queue
            # - Process orders
            # - Update order status
            while True:
                order = self.queue.get()
                if order is None:
                    self.output["shutdown"] = f"Worker {chef_id} shutting down..."
                    break
                
                self.output["preparing"] = f"chef {chef_id} started preparing Order #{order[0]}: {order[1]}"
                time.sleep(2)  # Simulate work
                self.output["complete"] = f"Order #{order[0]} completed by Chef {chef_id}"
                self.queue.task_done()

        def chef_output(self):
            with open("queue.txt", "w") as f:
                f.write(self.output.__str__())


        def create_order(self, order_id, dish_name):
            # TODO: Add orders to the queue
            self.queue.put((order_id, dish_name))

        def start_restaurant(self):
            for i in range(self.num_chefs):
                t = threading.Thread(target=self.chef_worker, args=(i,))
                t.start()
                self.chefs.append(t)
            pass

        def stop_restaurant(self):
            for _ in range(self.num_chefs):
                self.queue.put(None)
            for worker in self.chefs:
                worker.join()