from extract.base import BaseExtractor
from models.order import Order
from models.order_item import OrderItem
from common.database import engine
from sqlalchemy.orm import Session

class OrderItemExtractor(BaseExtractor):
    model = OrderItem
    @classmethod
    def extract_incremental(cls, last_run_time):
        with Session(engine) as session:
            rows = (
                session.query(OrderItem)
                .join(Order, OrderItem.order_id == Order.order_id)
                .filter(Order.created_at > last_run_time)
                .all()
            )

            return [
                row.to_dict()
                for row in rows
            
            ]