
from app.core.config import ALGORITHM, SECRET_KEY
from typing import Generator
from fastapi import HTTPException, Depends, Request
from sqlalchemy.orm import Session
from starlette import status
from jose import JWTError, jwt

from app.db import SessionLocal
from app.schemas.user import UserBase
from app.crud import user as crud_user

def get_db() -> Generator:

    """
    ## Dependency

    Generator for yielding db instances
    """

    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def auth_user(
    request: Request,
    db: Session = Depends(get_db),
) -> UserBase:
    """
    ## Dependency

    Authenticates a user by verifying their access token
    and returns the authenticated user info

    Returns
    --------
    user_id     : UUID
    email       : EmailStr
    master_pwd  : str
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    if (access_token := request.cookies.get("access_token")) is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="user not logged in"
        )
    try:
        payload = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
        if (user_info := payload.get("user_info")) is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    # check if user exists
    if (user := crud_user.get_user_by_id(db, user_info["uid"])) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="user does not exist"
        )
    return user
