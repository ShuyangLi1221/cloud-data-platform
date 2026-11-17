from load.base import BaseLoader

class OrderItemLoader(BaseLoader):

    table = "order_items"
    primary_key = "order_item_id"