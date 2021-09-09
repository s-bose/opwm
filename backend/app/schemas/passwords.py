from uuid import UUID
from typing import Optional
from pydantic import BaseModel, validator


class PasswordBase(BaseModel):
    pid: UUID
    site: Optional[str]
    link: Optional[str]
    username: Optional[str]
    password: Optional[str]

    @validator("pid")
    def uuid_validator_pk(cls, v):
        if v.version is None:
            raise ValueError("Invalid UUID")
        return str(v)


class PasswordInsert(BaseModel):
    site: str
    link: str
    username: str
    password: str


class PasswordUpdate(BaseModel):
    site: Optional[str]
    link: Optional[str]
    username: Optional[str]
    password: Optional[str]



if __name__ == "__main__":
    p1 = PasswordInsert(
        pid="0aa52950-f9e8-4fe1-b08f-2cef07f95729",
        username="user",
        password="pass",
    )
    print(p1)
    print(p1.dict(exclude_unset=True))
