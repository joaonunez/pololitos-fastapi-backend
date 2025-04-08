from pydantic import BaseModel
from datetime import datetime
from app.schemas.user_schema import UserSummary
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

    user: UserSummary
    class Config:
        from_attributes = True
