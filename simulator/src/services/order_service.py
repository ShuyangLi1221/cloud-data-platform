import random
from decimal import Decimal
from faker import Faker
from sqlalchemy.orm import Session
from common.database import engine
from enums.order_status import OrderStatus
from models.customer import Customer
from models.order import Order

fake = Faker("en_CA")

class OrderService:
    @staticmethod
    def seed(count: int) -> None:
        with Session(engine) as session:
            if session.query(Order).count() > 0:
                print("Orders already exists.")
                return
            
            customers = session.query(Customer).all()
            
            if not customers:
                raise Exception("No Customer Found. Seed Customer first.")
            
            orders = []
            
            for _ in range(count):
                
                customer = random.choice(customers)
                order = Order(
                    customer_id=customer.customer_id,
                    status=OrderService.random_status(),
                    total_amount=Decimal("0.00"),
                    order_date=fake.date_time_between(
                        start_date="-365d",
                        end_date="now"
                    )
                    
                )
                orders.append(order)
            session.add_all(orders)
            session.commit()
            print(f"{count} orders inserted.")
            
    
    
    @staticmethod
    def random_status() -> OrderStatus:

        return random.choices(
            population=[
                OrderStatus.OPEN,
                OrderStatus.WON,
                OrderStatus.LOST,
            ],
            weights=[10, 85, 5],
            k=1,
        )[0]
    
    @staticmethod
    def generate_daily() -> None:
        with Session(engine) as session:
            customers = session.query(Customer).all()
            
            if not customers:
                raise Exception("No customers found.")
            
            daily_orders = random.randint(50, 150)
            
            orders = []
            
            for _ in range(daily_orders):
                customer = random.choice(customers)
                order = Order(
                    customer_id=customer.customer_id,
                    status=OrderService.random_status(),
                    total_amount=Decimal("0.00"),
                    order_date=fake.date_time_between(
                        start_date="-1d",
                        end_date="now",
                    )
                )
                orders.append(order)
            
            session.add_all(orders)
            session.commit()
            
            print(f"{daily_orders} new orders inserted")