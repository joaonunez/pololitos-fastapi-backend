from pydantic import BaseModel
from datetime import datetime

class ServiceOut(BaseModel):
    id: int
    name: str
    description: str
    price: float
    city: str
    publish_date: datetime
    image_url: str | None
    user_id: int
    category_id: int

    class Config:
        from_attributes = True
