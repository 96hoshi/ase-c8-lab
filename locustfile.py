import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2) # 1-2 seconds between simulated events
    @task # defines a user task, associated to a microthread by locust
    def index_page(self):
            self.client.get("/") # get home page

    @task(3) # this task is 3 times likelier than the previous!
    def view_item(self):
        for item_id in range(10):
            self.client.get(f"/calc/sum?m={item_id}&n={42}", name="/calc/sum")
            time.sleep(1)

    @task(3) # this task is 3 times likelier than the previous!
    def view_item(self):
        for item_id in range(10):
            self.client.get(f"/calc/sub?m={item_id}&n={42}", name="/calc/sub")
            time.sleep(1)
    
    @task(3) # this task is 3 times likelier than the previous!
    def view_item(self):
        for item_id in range(10):
            self.client.get(f"/calc/mul?m={item_id}&n={42}", name="/calc/mul")
            time.sleep(1)

    @task(3) # this task is 3 times likelier than the previous!
    def view_item(self):
        for item_id in range(10):
            self.client.get(f"/calc/div?m={item_id}&n={42}", name="/calc/div")
            time.sleep(1)

