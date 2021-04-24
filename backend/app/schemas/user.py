from pydantic import BaseModel, EmailStr, SecretStr


class UserBase(BaseModel):
    id: str
    email: EmailStr
    master_pwd: str


class UserLogin(BaseModel):
    email: EmailStr
    master_pwd: str


class ResetPasswordForm(BaseModel):
    email: EmailStr
    new_password: str
