from extract.base import BaseExtractor
from models.order import Order

class OrderExtractor(BaseExtractor):
    model = Order
    incremental_column = Order.updated_at