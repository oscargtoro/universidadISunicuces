from locust import HttpUser, task

class LoadTest(HttpUser):
    @task
    def load(self):
        self.client.get("/")