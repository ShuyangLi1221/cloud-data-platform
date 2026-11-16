from pipeline.base import BasePipeline

from extract.order_item import OrderItemExtractor
from validate.order_item import OrderItemValidator
from transform.order_item import OrderItemTransformer
from load.order_item import OrderItemLoader

class OrderItemPipeline(BasePipeline):

    name = "order_items"

    extractor = OrderItemExtractor

    validator = OrderItemValidator

    transformer = OrderItemTransformer

    loader = OrderItemLoader