from uuid import UUID
from typing import Optional
from pydantic import BaseModel, validator


class PasswordBase(BaseModel):
    id: UUID
    site: str
    username: Optional[str] = None
    password: Optional[str] = None

    @validator("id")
    def uuid_validator_pk(cls, v):
        if v.version is None:
            raise ValueError("Invalid UUID")
        return str(v)


class PasswordInsert(BaseModel):
    site: str
    username: str
    password: str
