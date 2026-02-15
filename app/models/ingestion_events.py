from datetime import datetime, UTC

from sqlalchemy import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.core.domain.enums import IngestionTaskStatus
from app.database.base import Base


class IngestionEvent(Base):
    __tablename__ = "ingestion_events"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True
    )
    source: Mapped[str] = mapped_column(nullable=False)
    received_at: Mapped[datetime] = mapped_column(
        nullable=False,
        default=datetime.now(UTC)
    )
    status: Mapped[IngestionTaskStatus] = mapped_column(nullable=False)
    error: Mapped[str] = mapped_column(nullable=True)
    payload_hash: Mapped[str] = mapped_column(nullable=False, index=True)
    created_at: Mapped[datetime] = mapped_column(
        nullable=False,
        default=datetime.now(UTC)
    )