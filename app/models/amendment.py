from datetime import datetime, UTC

from sqlalchemy import UUID, ForeignKey, LargeBinary
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Amendment(Base):
    __tablename__ = "amendments"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True
    )
    filing_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("filings.id", ondelete="RESTRICT"),
        nullable=False,
        index=True
    )
    amended_filing_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("filings.id", ondelete="RESTRICT"),
        nullable=False,
        index=True
    )
    reason: Mapped[str] = mapped_column(nullable=False)
    version: Mapped[str] = mapped_column(nullable=False)
    raw_payload: Mapped[bytes] = mapped_column(LargeBinary, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        nullable=False,
        default=datetime.now(UTC)
    )

    filing: Mapped["Filing"] = relationship(
        back_populates="amendments"
    )