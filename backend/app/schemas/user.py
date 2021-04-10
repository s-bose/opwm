from pydantic import BaseModel, EmailStr, SecretStr


class UserModel(BaseModel):
    email: EmailStr
    master_pwd: str

    class Config:
        orm_mode = True
