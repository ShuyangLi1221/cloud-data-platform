from extract.base import BaseExtractor
from models.order_item import OrderItem


class OrderItemExtractor(BaseExtractor):
    model = OrderItem
    incremental_column = OrderItem.created_at