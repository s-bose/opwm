from pydantic import BaseModel, EmailStr, SecretStr
import uuid


class UserLogin(BaseModel):
    email: EmailStr
    master_pwd: SecretStr
