from uuid import UUID
from typing import Optional
from pydantic import BaseModel, validator


class PasswordBase(BaseModel):
    pid: UUID
    site: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None

    @validator("pid")
    def uuid_validator_pk(cls, v):
        if v.version is None:
            raise ValueError("Invalid UUID")
        return str(v)


class PasswordInsert(BaseModel):
    site: str
    username: str
    password: str
