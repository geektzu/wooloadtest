from locust import HttpUser, task, between
from locust.clients import HttpSession
from wootest import *


import time
# import itertools
# import random
# import names
# import random as r
# from faker import Faker
# fake = Faker()

# import urllib.request

# global_product_price_dict = {}
# global_product_link_dict = {}


def create_order():
  selenium_test()


# The real user class that will be instantiated and run by Locust
# This is the only thing that is actually specific to the service that we are testing.
class MyUser(HttpUser):
    wait_time = between(1, 2)
    def on_start(self):
        pass

    @task
    def buy(self):
        start_perf_counter = time.perf_counter()
        error = NameError('201 Status code not received')
        response_len = 0


        try: 
            create_order()
            error = None

            # if response.status_code == 201:
            #     response_len = len(response.text)
            #     error = None
            # else:
            #     error = NameError(str(response.status_code)+' status code')
        except Exception as e:
            error = e
            response = repr(e)

        response_time = (time.perf_counter() - start_perf_counter) * 1000
        
        name = "Add2Cart&Checkout"
        self.environment.events.request.fire(
            request_type="Selenium",
            name=name,
            response_time=response_time,
            response_length=response_len,
            exception=error,
            context=self.context(),
        )

    

    