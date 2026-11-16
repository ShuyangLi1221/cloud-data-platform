from datetime import datetime
from datetime import UTC
from sqlalchemy import Float, Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base

class EtlMetadata(Base):

    __tablename__ = "etl_metadata"

    pipeline_name: Mapped[str] = mapped_column(
        String,
        primary_key=True,
    )

    last_run: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="IDLE",
    )

    rows_loaded: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    duration_seconds: Mapped[float] = mapped_column(
        Float,
        default=0,
    )

    error_message: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
    )