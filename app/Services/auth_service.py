import bcrypt

from sqlalchemy.orm import Session
from app.Models.models import User
from app.Schemas.schemas import UserRegisterRequest
from app.Core.security import verify_password

def register_customer(
        db: Session,
        user_data: UserRegisterRequest
):
    existing_user = db.query(User).filter(User.username == user_data.username).first()
    if existing_user:
        raise ValueError("Tên đăng nhập đã tồn tại")

    hashed_password = bcrypt.hashpw(user_data.password.encode('utf-8'), bcrypt.gensalt())

    new_user = User(
        username=user_data.username,
        password=hashed_password,
        role=user_data.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return None

    password_correct = verify_password(password, user.hashed_password)
    if not password_correct:
        return None
    return user