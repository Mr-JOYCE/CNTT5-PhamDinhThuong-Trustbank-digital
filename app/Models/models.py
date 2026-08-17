from sqlalchemy import Column, Integer, String, DateTime, Enum, func

from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(Enum("admin", "customer", name="user_roles"), nullable=False, default="customer")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
