from faker import Faker
from sqlalchemy.orm import Session
from sqlalchemy import select, func
from common.database import engine
from models.customer import Customer
import random
from sqlalchemy.dialects.postgresql import insert

fake = Faker("en_CA")


class CustomerService:
    @staticmethod
    def seed(count: int):
        customers = []
        
        for _ in range(count):
            customer = Customer(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.unique.email(),
                phone=fake.phone_number(),
                city=fake.city(),
                province=fake.province(),
            )
            
            customers.append(customer)
            
        with Session(engine) as session:
            customer_count = session.scalar(
                select(func.count()).select_from(Customer)
            )
            if customer_count > 0:
                print(f"Customer Table Already has {customer_count} customers, skip creation...")
            else:
                session.add_all(customers)
                session.commit()
                print(f"{count} customers inserted")
    
    @staticmethod
    def generate_daily() -> None:
        daily_count = random.randint(1, 5)
        
        customers = []
        
        for _ in range(daily_count):
            customer = Customer(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.unique.email(),
                phone=fake.phone_number(),
                city=fake.city(),
                province=fake.province(),
            )
            customers.append(customer)
        data = [
            {
                "first_name": c.first_name,
                "last_name": c.last_name,
                "email": c.email,
                "phone": c.phone,
                "city": c.city,
                "province": c.province,
            }
            for c in customers
        ]
        
        with Session(engine) as session:
            stmt = (
                insert(Customer)
                .values(data)
                .on_conflict_do_nothing(index_elements=["email"])
            )
            result = session.execute(stmt)
            session.commit()
        
        print(f"{result.rowcount} new customers inserted")