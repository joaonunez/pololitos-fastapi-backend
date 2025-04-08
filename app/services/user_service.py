from passlib.hash import bcrypt
from sqlmodel import Session, select
from app.models.user_model import User

def login_user(session: Session, email: str, password: str):
    user = session.exec(select(User).where(User.email == email)).first()
    if user and bcrypt.verify(password, user.password):
        return user
    return None
