from datetime import timedelta
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Request
)
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from starlette import status

from app.security import create_access_token, get_hash

from app.crud import crudUsers
from app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES
from app.api.dependency import get_db, auth_user

from app.schemas.user import UserLogin, UserModel
router = APIRouter()


"""
TODO 
implement a max no of login trials before login gets blocked

"""


@router.post("/register")
def register(
    cred: UserLogin,
    db: Session = Depends(get_db)
):
    pwd = get_hash(cred.master_pwd)       # hash once in the server
    print(pwd)
    # hash of the hash stored in db
    _id = crudUsers.post_user(db, email=cred.email, password=pwd)

    return {
        "id": _id
    }


@router.post("/login")
def login(
    cred: UserLogin,
    db: Session = Depends(get_db)
) -> None:
    """
    post user credentials (email & master password) to log in.
    The master password is hashed once in the server using bcrypt
    and upon insertion, it is hashed again at the postgres db
    using md5 by the pgcrypto extension.

    generates an access token upon login and sets response cookie

    """
    user_email = cred.email
    user_pass = cred.master_pwd

    pwd = get_hash(user_pass)
    print(pwd)
    if (user_id := crudUsers.get_user_by_email(db, cred.email)) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="email not found"
        )

    if (user := crudUsers.get_user(db, user_email, pwd)) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="invalid email/password"
        )

    # token expires after X minutes
    time_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {
        "user": UserModel(**user).dict()
    }

    access_token = create_access_token(                             # create a jwt access token
        data=payload,
        expires_delta=time_expires
    )

    response = JSONResponse(content=payload)
    response.set_cookie(key="access_token",
                        value=access_token)

    return response


@router.get("/user")
def get_user_info(
    request: Request,
    user: UserModel = Depends(auth_user),
    db: Session = Depends(get_db)
):
    return {
        "user": user
    }
