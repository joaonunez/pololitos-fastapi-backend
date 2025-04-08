# app/schemas/user_schema.py
from pydantic import BaseModel

class UserSummary(BaseModel):
    id: int
    first_name: str
    last_name: str

    class Config:
        from_attributes = True
