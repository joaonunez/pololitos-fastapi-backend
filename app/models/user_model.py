from __future__ import annotations
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from .base import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    phone = Column(String(20))
    city = Column(String(100))
    profile_picture = Column(String)


    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    services = relationship("Service", back_populates="user", cascade="all, delete-orphan")
    requests = relationship("Request", back_populates="requester", cascade="all, delete-orphan")
    reviews = relationship("Review", back_populates="user")
