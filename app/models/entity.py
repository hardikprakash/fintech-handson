from datetime import datetime, UTC
from typing import List

from sqlalchemy import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.domain.enums import EntityType
from app.database.base import Base


class Entity(Base):
    __tablename__ = "entities"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True
    )
    entity_type: Mapped[EntityType] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        nullable=False,
        default=datetime.now(UTC)
    )

    filings: Mapped[List["Filing"]] = relationship(
        back_populates="entity"
    )