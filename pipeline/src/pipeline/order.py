from pipeline.base import BasePipeline
from extract.order import OrderExtractor
from validate.order import OrderValidator
from transform.order import OrderTransformer
from load.order import OrderLoader

class OrderPipeline(BasePipeline):

    name = "orders"

    extractor = OrderExtractor

    validator = OrderValidator

    transformer = OrderTransformer

    loader = OrderLoader