from locust import HttpUser, task


class WebsiteUser(HttpUser):

    @task(10)
    def index(self):
        self.client.get("/")

    @task(5)
    def products(self):
        self.client.get("/produtos/")

    @task(2)
    def flyers(self):
        self.client.get("/folhetos/")

    @task(2)
    def order(self):
        self.client.get("/produtos/comida-fresca-takeaway/encomendas/menu-seleccao-do-chef/#2")
