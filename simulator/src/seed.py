from sqlalchemy import text

from common.database import engine
from models.base import Base
import models

from services.customer_service import CustomerService
from services.product_service import ProductService
from services.order_service import OrderService
from services.order_item_service import OrderItemService


def main():
    print("Creating tables...")

    Base.metadata.create_all(engine)

    print("Tables created successfully.")

    print("Seeding customers....")
    CustomerService.seed(1000)
    
    print("Seeding products....")
    ProductService.seed()
    
    print("Seeding orders....")
    OrderService.seed(2100)
    
    print("Seeding order items....")
    OrderItemService.seed()
    print("Done.")
    
    

if __name__ == "__main__":
    main()