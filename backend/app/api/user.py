from fastapi import APIRouter, Depends, Request
from pydantic import EmailStr

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
    email: EmailStr,
    password: str
) -> None:
    """
    logs in
    """
    return None


@router.put("/user")
def user() -> None:
    return None


@router.post("/reset_pwd")
def reset_master_pwd() -> None:
    return None
