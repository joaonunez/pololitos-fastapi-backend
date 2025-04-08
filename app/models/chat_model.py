from __future__ import annotations
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Chat(SQLModel, table=True):
    __tablename__ = "chat"
    model_config = {
        "arbitrary_types_allowed": True
    }

    id: str = Field(primary_key=True)
    name: str
    creation_timestamp: int
    requester_id: Optional[int] = None
    request_id: Optional[int] = None
