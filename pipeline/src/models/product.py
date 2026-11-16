from datetime import datetime
from decimal import Decimal
from sqlalchemy import Enum, String, Numeric, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from typing import TYPE_CHECKING

from enums.product_category import ProductCategory

if TYPE_CHECKING:
    from models.order_item import OrderItem


class Product(Base):

    __tablename__ = "products"

    product_id: Mapped[int] = mapped_column(primary_key=True)

    sku: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        index=True,
    )

    brand: Mapped[str] = mapped_column(
        String(50),
        index=True,
    )

    category: Mapped[ProductCategory] = mapped_column(
        Enum(ProductCategory),
        nullable=False,
    )

    product_name: Mapped[str] = mapped_column(
        String(150)
    )

    price: Mapped[Decimal] = mapped_column(
        Numeric(10, 2)
    )

    cost: Mapped[Decimal] = mapped_column(
        Numeric(10, 2)
    )

    inventory: Mapped[int] = mapped_column(
        default=100
    )

    is_active: Mapped[bool] = mapped_column(
        default=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    order_items: Mapped[list["OrderItem"]] = relationship(
        back_populates="product"
    )