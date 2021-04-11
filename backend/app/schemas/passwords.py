from typing import List
from pydantic import BaseModel


class PasswordModel(BaseModel):
    site: str
    user_id: int
    username: str
    password: str


class PasswordInsert(BaseModel):
    site: str
    username: str
    password: str
