from __future__ import annotations
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from .base import Base

class Review(Base):
    __tablename__ = "review"

    id = Column(Integer, primary_key=True, index=True)
    rating = Column(Integer, nullable=False)
    comment = Column(String, nullable=True)

    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    service_id = Column(Integer, ForeignKey("service.id"), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relaciones
    user = relationship("User", back_populates="reviews")
    service = relationship("Service", back_populates="reviews")
