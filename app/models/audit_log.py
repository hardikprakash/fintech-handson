from datetime import datetime, UTC
from typing import Optional

from sqlalchemy import UUID, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.core.domain.enums import AuditAction, AuditEntityType
from app.database.base import Base


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True
    )
    actor: Mapped[str] = mapped_column(nullable=False)
    action: Mapped[AuditAction] = mapped_column(nullable=False, index=True)
    entity_type: Mapped[AuditEntityType] = mapped_column(nullable=False, index=True)
    entity_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        nullable=False,
        index=True
    )
    timestamp: Mapped[datetime] = mapped_column(
        nullable=False,
        default=datetime.now(UTC),
        index=True
    )
    old_value: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    new_value: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
