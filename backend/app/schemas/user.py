from typing import Optional
from pydantic import BaseModel, EmailStr, validator
from uuid import UUID


class UserBase(BaseModel):
    id: UUID
    email: EmailStr
    master_pwd: Optional[str] = None

    @validator("id")
    def uuid_pk_validator(cls, v):
        if v.version is None:
            raise ValueError("Invalid UUID")
        return str(v)


class UserLogin(BaseModel):
    email: EmailStr
    master_pwd: str


class ResetPasswordForm(BaseModel):
    email: EmailStr
    new_password: str
