from __future__ import annotations
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy.orm import Mapped
from typing import Optional, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from .user_model import User
    from .service_model import Service

class Request(SQLModel, table=True):
    __tablename__ = "request"
    model_config = {
        "arbitrary_types_allowed": True
    }

    id: Optional[int] = Field(default=None, primary_key=True)
    status: str
    request_date: datetime = Field(default_factory=datetime.utcnow)
    additional_comment: Optional[str] = None

    requester_id: int = Field(foreign_key="user.id")
    service_id: int = Field(foreign_key="service.id")

    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

    requester: Mapped["User"] = Relationship(back_populates="requests")
    service: Mapped["Service"] = Relationship()
