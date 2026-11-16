from extract.base import BaseExtractor
from models.product import Product

class ProductExtractor(BaseExtractor):
    model = Product
    incremental_column = Product.created_at