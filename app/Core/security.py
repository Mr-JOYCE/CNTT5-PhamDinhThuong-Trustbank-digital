import os
import re 
import bcrypt

from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import jwt

load_dotenv()

SECRET_KEY = os.getenv("TRUSTBANK_SECRET_KEY")
if not SECRET_KEY:
    raise RuntimeError(
        "TRUSTBANK_SECRET_KEY chưa dược thiết lập trong biến môi trường. Vui lòng thêm TRUSTBANK_SECRET_KEY vào tệp .env"
    )

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 10

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def create_access_token(username: str, role:str) -> str:
    now = datetime.now(timezone.utc)
    expire = now + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    payload = {
        "sub": username,
        "role": role,
        "iat": now.timestamp(),
        "exp": expire.timestamp()
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

