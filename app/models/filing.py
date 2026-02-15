from datetime import datetime, UTC
from typing import List

from sqlalchemy import UUID, ForeignKey, LargeBinary
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.domain.enums import FilingType
from app.database.base import Base


class Filing(Base):
    __tablename__ = "filings"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True
    )
    entity_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("entities.id", ondelete="RESTRICT"),
        nullable=False,
        index=True
    )
    filing_type: Mapped[FilingType] = mapped_column(nullable=False)
    filed_by: Mapped[str] = mapped_column(nullable=False)
    raw_payload: Mapped[bytes] = mapped_column(LargeBinary, nullable=False)

    version: Mapped[str] = mapped_column(nullable=False)
    is_amended: Mapped[bool] = mapped_column(nullable=False, default=False)
    created_at: Mapped[datetime] = mapped_column(
        nullable=False,
        default=datetime.now(UTC)
    )

    entity: Mapped["Entity"] = relationship(
        back_populates="filings"
    )

    amendments: Mapped[List["Amendment"]] = relationship(
        back_populates="filing"
    )