from __future__ import annotations
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional
from datetime import datetime

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .user_model import User
    from .service_model import Service

class Review(SQLModel, table=True):
    __tablename__ = "review"
    model_config = {
        "arbitrary_types_allowed": True
    }

    id: Optional[int] = mapped_column(primary_key=True)
    rating: Mapped[int] = mapped_column(ge=1, le=5, description="Calificación entre 1 y 5 estrellas")
    comment: Mapped[Optional[str]] = mapped_column(default=None)

    user_id: Mapped[int] = mapped_column(foreign_key="user.id")
    service_id: Mapped[int] = mapped_column(foreign_key="service.id")

    created_at: Mapped[Optional[datetime]] = mapped_column(default_factory=datetime.utcnow)
    updated_at: Mapped[Optional[datetime]] = mapped_column(default_factory=datetime.utcnow)

    user: Mapped["User"] = Relationship()
    service: Mapped["Service"] = Relationship()
