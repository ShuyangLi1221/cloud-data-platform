from sqlalchemy import ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base import Base
from typing import TYPE_CHECKING
from decimal import Decimal

if TYPE_CHECKING:
    from models.order import Order
    from models.product import Product

class OrderItem(Base):
    __tablename__="order_items"
    
    order_item_id: Mapped[int] = mapped_column(primary_key=True)
    
    order_id: Mapped[int] = mapped_column(
        ForeignKey("orders.order_id"),
        index=True
    )
    
    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.product_id"),
        index=True,
    )

    quantity: Mapped[int] = mapped_column()

    unit_price: Mapped[Decimal] = mapped_column(
        Numeric(10, 2)
    )

    line_total: Mapped[Decimal] = mapped_column(
        Numeric(10, 2)
    )

    order: Mapped["Order"] = relationship(back_populates="order_items")
    product: Mapped["Product"] = relationship(back_populates="order_items")
    