from __future__ import annotations
from typing import Optional, List, TYPE_CHECKING
from datetime import datetime
from sqlmodel import SQLModel, Relationship
from sqlalchemy.orm import Mapped, mapped_column

if TYPE_CHECKING:
    from .service_model import Service

class Category(SQLModel, table=True):
    __tablename__ = "category"
    model_config = {
        "arbitrary_types_allowed": True
    }

    id: Optional[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

    created_at: Mapped[Optional[datetime]] = mapped_column(default_factory=datetime.utcnow)
    updated_at: Mapped[Optional[datetime]] = mapped_column(default_factory=datetime.utcnow)

    services: Mapped[List["Service"]] = Relationship(back_populates="category")
