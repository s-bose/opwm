import uuid
from pydantic import BaseModel, SecretStr


class PasswordInsert(BaseModel):
    site: str
    username: str
    password: str
