from passlib.hash import bcrypt
from fastapi import UploadFile, HTTPException
from sqlmodel import Session, select
from app.models.user_model import User
from app.services.cloudinary_service import upload_file, delete_file
def login_user(session: Session, email: str, password: str):
    user = session.exec(select(User).where(User.email == email)).first()
    if user and bcrypt.verify(password, user.password):
        return user
    return None

def get_user_by_id(db: Session, user_id: int) -> User | None:
    return db.get(User, user_id)

def update_user(db: Session, user: User) -> User:
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


async def update_user_profile(
    db: Session,
    user_id: int,
    first_name: str,
    last_name: str,
    city: str,
    phone: str,
    profile_image_file: UploadFile = None
) -> User:
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=401, detail="Usuario no encontrado.")

    # Imagen
    if profile_image_file:
        if user.profile_picture:
            await delete_file(user.profile_picture)

        try:
            new_url = await upload_file(profile_image_file, folder="profile-images")
            user.profile_picture = new_url
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error al subir imagen: {str(e)}")

    # Otros campos
    user.first_name = first_name
    user.last_name = last_name
    user.city = city
    user.phone = phone

    return update_user(db, user)