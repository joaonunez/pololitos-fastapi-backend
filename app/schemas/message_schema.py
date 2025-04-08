from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Message(BaseModel):
    id: Optional[str]
    content: str
    userId: int
    userName: str
    createdAt: Optional[str] = datetime.utcnow().isoformat()
