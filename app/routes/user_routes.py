from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.schemas.login_schema import LoginUserRequest, LoginUserResponse
from app.auth.jwt_handler import create_token
from app.services.user_service import login_user
from app.core.db import get_db

router = APIRouter(prefix="/api/users", tags=["Users"])

@router.post("/login", response_model=LoginUserResponse)
def login_user_route(payload: LoginUserRequest, db: Session = Depends(get_db)):
    user = login_user(db, payload.email, payload.password)
    if not user:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    token = create_token({"sub": user.email, "id": user.id})

    return LoginUserResponse(
        id=user.id,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        profile_picture=user.profile_picture or "",
        phone=user.phone,
        city=user.city,
        token=token
    )
