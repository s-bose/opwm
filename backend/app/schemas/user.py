from pydantic import BaseModel, EmailStr, SecretStr


class UserModel(BaseModel):
    id: int
    email: EmailStr


class UserLogin(BaseModel):
    email: EmailStr
    master_pwd: str
