from load.base import BaseLoader

class CustomerLoader(BaseLoader):
    table = "customers"
    primary_key = "customer_id"