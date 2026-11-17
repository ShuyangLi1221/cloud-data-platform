from load.base import BaseLoader

class OrderLoader(BaseLoader):

    table = "orders"
    primary_key = "order_id"