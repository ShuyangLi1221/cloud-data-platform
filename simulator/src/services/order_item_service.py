import random
from decimal import Decimal
from sqlalchemy.orm import Session
from common.database import engine
from models.order import Order
from models.order_item import OrderItem
from models.product import Product

class OrderItemService:
    
    @staticmethod
    def seed() -> None:
        
        with Session(engine) as session:
            if session.query(OrderItem).count()>0:
                print("Order Items already exist.")
            
            orders = session.query(Order).all()
            products = session.query(Product).all()
            
            if not orders:
                raise Exception("No orders found")
            if not products:
                raise Exception("No products found")
            
            order_items = []
            
            for order in orders:
                
                selected_products = random.sample(
                    products,
                    k=random.randint(1, 3)
                )
                order_total = Decimal("0.00")
                
                for product in selected_products:
                    quantity = random.randint(1,3)
                    
                    line_total = product.price * quantity
                    
                    item = OrderItem(
                        order_id = order.order_id,
                        product_id = product.product_id,
                        quantity = quantity,
                        unit_price = product.price,
                        line_total = line_total
                    )
                    order_items.append(item)
                    order_total += line_total
                
                order.total_amount = order_total
                
            session.add_all(order_items)

            session.commit()

            print(f"{len(order_items)} order items inserted.")
    
    def generate_daily() -> None:
        with Session(engine) as session:
            orders = (
                session.query(Order)
                .filter(~Order.order_items.any())
                .all()
            )
            
            products = session.query(Product).all()
            
            total_items = 0
            
            for order in orders:
                order_total = Decimal("0.00")
                item_count = random.randint(1, 3)
                selected_products = random.sample(products, k=item_count)
                
                for product in selected_products:
                    quantity = random.randint(1, 3)
                    line_total = product.price * quantity
                    
                    item = OrderItem(
                        order_id = order.order_id,
                        product_id = product.product_id,
                        quantity = quantity,
                        unit_price = product.price,
                        line_total = line_total,
                    )
                    
                    session.add(item)
                    
                    order_total += line_total
                    total_items += 1
                
                order.total_amount = order_total
            
            session.commit()
            
            print(
                f"{len(orders)} orders, "
                f"{total_items} order items generated."
            )