from fastapi import APIRouter, Depends, Request
from pydantic import EmailStr

from sqlalchemy.orm import Session

from app.crud.usersCrud import get_user
from app.api.dependency import get_db

router = APIRouter()


@router.post("/register")
def register(
    name: str,
    email: EmailStr,
    password: str
) -> None:
    """
    registers a user with email and master password
    """
    return None


@router.get("/login")
def login(
    db: Session = Depends(get_db),
    *,
    email: EmailStr,
    password: str
) -> None:
    """
    logs in
    TODO needs oauth2 formdata impl here
    """
    return get_user(db, 'abc@abc.com', 'hello')


@router.put("/user")
def user() -> None:
    return None


@router.post("/reset_pwd")
def reset_master_pwd() -> None:
    return None
