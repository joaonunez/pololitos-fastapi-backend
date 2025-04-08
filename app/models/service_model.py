from __future__ import annotations
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy.orm import Mapped
from typing import Optional, TYPE_CHECKING
from datetime import datetime
from .category_model import Category

if TYPE_CHECKING:
    from .user_model import User

class Service(SQLModel, table=True):
    __tablename__ = "service"
    model_config = {
        "arbitrary_types_allowed": True
    }

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=10)
    price: float
    city: str
    publish_date: datetime = Field(default_factory=datetime.utcnow)
    image_url: Optional[str] = None

    user_id: int = Field(foreign_key="user.id")
    category_id: int = Field(foreign_key="category.id")

    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

    user: Mapped["User"] = Relationship(back_populates="services")
    category: Mapped[Category] = Relationship(back_populates="services")
