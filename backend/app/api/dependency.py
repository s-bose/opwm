from app.models.user import User
from app.crud import crudUsers
from app.core.config import ALGORITHM, SECRET_KEY
from typing import Generator
from fastapi import HTTPException, Depends, Request
from sqlalchemy.orm import Session
from starlette import status
from jose import JWTError, jwt

from app.db import SessionLocal


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def auth_user(
    request: Request,
    db: Session = Depends(get_db),
):
    """
    Authenticates a user by verifying their access token

    ## Dependency
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
        if (user := payload.get("user")) is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    if (user := crudUsers.get_user_by_id(db, str(user["id"]))) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="user does not exist"
        )
    return User(**user)
