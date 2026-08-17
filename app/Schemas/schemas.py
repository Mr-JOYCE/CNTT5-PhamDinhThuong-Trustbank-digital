from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict

class UserRegisterRequest(BaseModel):
    username: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Tên đăng nhập"
    )

    password: str = Field(
        ...,
        min_length=6,
        max_length=100,
        description="Mật khẩu"
    )

    role: str = Field(
        default="customer",
        description="Vai trò của tài khoản"
    )

class UserLoginRequest(BaseModel):
    username: str = Field(
        ...,
        min_length=3,
        max_length=50
    )

    password: str = Field(
        ...,
        min_length=6,
        max_length=100
    )

class ChangePasswordRequest(BaseModel):
    old_password: str = Field(
        ...,
        min_length=6,
        max_length=100
    )

    new_password: str = Field(
        ...,
        min_length=6,
        max_length=100
    )

class TransferRequest(BaseModel):
    to_username: str = Field(
        ...,
        min_length=3,
        max_length=50
    )

    amount: Decimal = Field(
        ...,
        gt=0,
        description="Số tiền chuyển phải lớn hơn 0"
    )

    note: Optional[str] = Field(
        default=None,
        max_length=255
    )

class UserResponse(BaseModel):
    id: int
    username: str
    role: str
    balance: Decimal
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class BalanceResponse(BaseModel):
    username: str
    balance: Decimal

    model_config = ConfigDict(
        from_attributes=True
    )

class TransferResponse(BaseModel):
    id: int
    from_username: str
    to_username: str
    amount: Decimal
    note: Optional[str] = None
    status: str

    model_config = ConfigDict(
        from_attributes=True
    )


class UserAdminResponse(BaseModel):
    id: int
    username: str
    role: str
    balance: Decimal
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )