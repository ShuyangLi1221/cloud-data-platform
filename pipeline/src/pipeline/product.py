from pipeline.base import BasePipeline
from extract.product import ProductExtractor
from validate.product import ProductValidator
from transform.product import ProductTransformer
from load.product import ProductLoader

class ProductPipeline(BasePipeline):
    
    name = "products"
    
    extractor = ProductExtractor
    
    validator = ProductValidator
    
    transformer = ProductTransformer
    
    loader = ProductLoader