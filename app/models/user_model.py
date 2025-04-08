from __future__ import annotations
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy.orm import Mapped
from typing import Optional, List, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from .service_model import Service
    from .request_model import Request

class User(SQLModel, table=True):
    __tablename__ = "user"
    model_config = {
        "arbitrary_types_allowed": True
    }

    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str = Field(min_length=3)
    last_name: str = Field(min_length=3)
    email: str
    password: str
    phone: str
    city: str
    profile_image: Optional[str] = None

    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

    services: Mapped[List["Service"]] = Relationship(back_populates="user")
    requests: Mapped[List["Request"]] = Relationship(back_populates="requester")
