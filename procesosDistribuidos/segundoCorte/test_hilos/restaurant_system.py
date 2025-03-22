import threading
from queue import Queue
import time
import random

class Restaurant:
    def __init__(self):
        # TODO: Initialize the restaurant system
        # - Create order queue
        # - Initialize chef threads
        self.queue = Queue()
        self.chefs = []
        self.num_chefs = 3

    def chef_worker(self, chef_id):
        # TODO: Implement chef behavior
        # - Get orders from queue
        # - Process orders
        # - Update order status
        while True:
            order = random.choice(self.queue.get())
            if order is None:
                print(f"Worker {chef_id} shutting down...")
                break
            
            print(f"chef {chef_id} started preparing Order #{order[0]}")
            time.sleep(2)  # Simulate work
            print(f"Order #{order[1]} completed by Chef {chef_id}")
            self.queue.task_done()

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

def main():
    # TODO: Create and run the restaurant system
    restaurante = Restaurant()
    restaurante.start_restaurant()

    # Add some example tasks
    for i in range(10):
        restaurante.create_order(i, f"dish {i}")

    # Wait for all tasks to complete
    restaurante.queue.join()
    restaurante.stop_restaurant()

if __name__ == "__main__":
    main()



# salida esperada
# Chef 1 started preparing Order #2: Pizza (Est. time: 3 min)
# Chef 2 started preparing Order #1: Pasta (Est. time: 2 min)
# Chef 3 started preparing Order #3: Salad (Est. time: 1 min)
# Order #3 completed by Chef 3
# Chef 3 started preparing Order #4: Soup...



# This exercise is effective because:
# 1. It relates to a real-world scenario students can understand
# 2. It covers fundamental threading concepts
# 3. It has different difficulty levels
# 4. It's extensible with bonus challenges
# 5. It encourages problem-solving and creativity
