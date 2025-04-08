from __future__ import annotations
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from .base import Base

class Request(Base):
    __tablename__ = "request"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String(50), nullable=False)
    request_date = Column(DateTime, default=datetime.utcnow)
    additional_comment = Column(String, nullable=True)

    requester_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    service_id = Column(Integer, ForeignKey("service.id"), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relaciones
    requester = relationship("User", back_populates="requests")
    service = relationship("Service")
