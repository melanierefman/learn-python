import random
from locust import HttpUser, task, between

# class JSONPlaceholderUser(HttpUser):
#     wait_time = between(1, 3)
#     host = "https://jsonplaceholder.typicode.com"

#     @task(3)
#     def get_all_posts(self):
#         self.client.get("/posts")

#     @task(2)
#     def get_single_post(self):
#         post_id = random.randint(1, 100)
#         self.client.get(f"/posts/{post_id}", name="/posts/[id]")

#     @task(1)
#     def get_comments_by_post(self):
#         post_id = random.randint(1, 100)
#         self.client.get(
#             f"/comments?postId={post_id}",
#             name="/comments?postId=[id]"
#         )


class DummyJsonUser(HttpUser):
    # Base URL for the DummyJSON API
    host = "https://dummyjson.com"

    # Simulate a wait time of 1 to 5 seconds between tasks
    wait_time = between(1, 5)

    @task(3)
    def get_all_products(self):
        """Fetch all products (GET request) - weighted heavier"""
        self.client.get("/products")

    @task(2)
    def get_single_product(self):
        """Fetch a specific random product ID from 1 to 100 (GET request)"""
        product_id = random.randint(1, 100)
        self.client.get(f"/products/{product_id}")

    @task(1)
    def add_new_product(self):
        """Add a new dummy product (POST request)"""
        payload = {"title": "Test Product", "category": "beauty", "price": 29.99}

        headers = {"Content-Type": "application/json"}

        self.client.post("/products/add", json=payload, headers=headers)