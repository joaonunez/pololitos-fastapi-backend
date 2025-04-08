from fastapi import APIRouter, Depends, HTTPException, UploadFile, Form, File, status
from app.auth.jwt_bearer import get_current_user_id
from sqlmodel import Session
from app.schemas.login_schema import LoginUserRequest, LoginUserResponse
from app.auth.jwt_handler import create_token




from app.services.user_service import login_user, update_user_profile
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

@router.patch("/profile/update")
async def update_profile(
    first_name: str = Form(...),
    last_name: str = Form(...),
    city: str = Form(...),
    phone: str = Form(...),
    profile_image_file: UploadFile = File(None),
    user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db)
):
    updated_user = await update_user_profile(
        db=db,
        user_id=user_id,
        first_name=first_name,
        last_name=last_name,
        city=city,
        phone=phone,
        profile_image_file=profile_image_file
    )

    return {
        "id": updated_user.id,
        "email": updated_user.email,
        "first_name": updated_user.first_name,
        "last_name": updated_user.last_name,
        "phone": updated_user.phone,
        "city": updated_user.city,
        "profile_picture": updated_user.profile_picture
    }
