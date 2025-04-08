from pydantic import BaseModel, EmailStr, Field

class LoginUserRequest(BaseModel):
    email: EmailStr = Field(..., example="test@mail.com")
    password: str = Field(..., min_length=6)

class LoginUserResponse(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    profile_image: str
    phone: str
    city: str
    token: str
