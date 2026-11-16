from pipeline.base import BasePipeline
from extract.customer import CustomerExtractor
from validate.customer import CustomerValidator
from transform.customer import CustomerTransformer
from load.customer import CustomerLoader

class CustomerPipeline(BasePipeline):
    
    name = "customers"
    
    extractor = CustomerExtractor
    validator = CustomerValidator
    
    transformer = CustomerTransformer
    
    loader = CustomerLoader