from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from starlette import status


from app.models.user import User
from app.security import create_access_token, get_hash
from app.crud import crudUsers
from app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES
from app.api.dependency import get_db, auth_user
from app.schemas.user import UserLogin

router = APIRouter()


"""
TODO 
implement a max no of login trials before login gets blocked
"""


@router.post("/register")
def register(cred: UserLogin, db: Session = Depends(get_db)):

    """
    ## API Register

    Registers a new user into the system by storing their email &
    master password (hash) in the database

    The plaintext master password credential is first hashed once
    at the API.

    This hash is done using a fixed salt so that for subsequent
    login, the same mid-hash is generated from the login credentials
    in order to verify the mid-hash with the final-hash in the db.

    The resulting hash is then further hashed at the database.


    Parameters
    ----------

    cred : <email, master_pwd>


    Returns
    -------

    id
    """
    pwd = get_hash(cred.master_pwd.get_secret_value())  # hash once in the server
    # hash of the hash stored in db
    _id = crudUsers.post_user(db, email=cred.email, password=pwd)

    return _id


@router.post("/login")
def login(cred: UserLogin, db: Session = Depends(get_db)):

    """
    ## API Login

    post user credentials (email & master password) to log in.
    The master password is hashed once in the server using bcrypt
    and upon insertion, it is hashed again at the postgres db
    using md5 by the pgcrypto extension.

    generates an access token upon login and sets response cookie

    """
    user_email = cred.email
    user_pass = cred.master_pwd.get_secret_value()

    pwd = get_hash(user_pass)
    if (user_id := crudUsers.get_user_by_email(db, cred.email)) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="email not found"
        )

    if (user := crudUsers.get_user(db, user_email, pwd)) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="invalid email/password"
        )

    # token expires after X minutes
    time_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {"user": {"id": str(user.id), "email": user.email}}

    access_token = create_access_token(  # create a jwt access token
        data=payload, expires_delta=time_expires
    )

    response = JSONResponse(content=payload)
    response.set_cookie(
        key="access_token", value=access_token, max_age=time_expires.total_seconds()
    )

    return response


@router.get("/user")
def get_user_info(user: User = Depends(auth_user), db: Session = Depends(get_db)):
    return {"user_id": user.id, "email": user.email}


@router.post("/reset_password")
def reset_password(
    user: User = Depends(auth_user),
    db: Session = Depends(get_db),
):

    # check if user has any recovery email in their account
    if user.recovery_email is None:
        print("lol")
