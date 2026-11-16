from datetime import datetime
from decimal import Decimal
from sqlalchemy import DateTime, ForeignKey, Numeric, String, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from enums.order_status import OrderStatus
from models.base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.customer import Customer
    from models.order_item import OrderItem
    
class Order(Base):
    __tablename__ = "orders"
    
    order_id: Mapped[int] = mapped_column(primary_key=True)
    
    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customers.customer_id"), 
        index=True
    )
    
    status: Mapped[OrderStatus] = mapped_column(
        Enum(OrderStatus, name="order_status"),
        default=OrderStatus.OPEN,
        nullable=False
    )
    
    total_amount: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    
    order_date: Mapped[datetime] = mapped_column(DateTime, default = datetime.utcnow)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    
    customer: Mapped["Customer"] = relationship(back_populates="orders")
    
    order_items: Mapped[list["OrderItem"]] = relationship(
        back_populates="order",
        cascade="all, delete-orphan",
    )