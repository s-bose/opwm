from pydantic import BaseModel, EmailStr, SecretStr
import uuid


class UserModel(BaseModel):
    id: uuid.UUID
    email: EmailStr


class UserLogin(BaseModel):
    email: EmailStr
    master_pwd: str
