from __future__ import annotations
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

from .base import Base

class Chat(Base):
    __tablename__ = "chats"

    id = Column(String, primary_key=True, index=True)  # ID generado en Firebase o UUID
    name = Column(String, nullable=False)
    creation_timestamp = Column(Integer, nullable=False)  # UNIX timestamp

    requester_id = Column(Integer, nullable=True)
    request_id = Column(Integer, nullable=True)
