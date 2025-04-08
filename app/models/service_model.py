from __future__ import annotations
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from .base import Base

class Service(Base):
    __tablename__ = "service"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    city = Column(String(100), nullable=False)
    publish_date = Column(DateTime, default=datetime.utcnow)
    image_url = Column(String, nullable=True)

    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("category.id"), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relaciones
    user = relationship("User", back_populates="services")
    category = relationship("Category", back_populates="services")
    reviews = relationship("Review", back_populates="service")

