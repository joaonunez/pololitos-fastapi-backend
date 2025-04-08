from pydantic import BaseModel
from typing import Optional

class Notification(BaseModel):
    id: Optional[str]
    receiverId: int
    type: str
    message: str
    targetUrl: str
    read: bool = False
    timestamp: Optional[str]
    senderId: int
    senderName: str
    serviceName: str
    serviceImage: str
