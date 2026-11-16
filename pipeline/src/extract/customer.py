from extract.base import BaseExtractor
from models.customer import Customer

class CustomerExtractor(BaseExtractor):
    
    model = Customer
    incremental_column = Customer.created_at
    
