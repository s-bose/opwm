from typing import Any, Dict
from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.responses import JSONResponse
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError

from sqlalchemy.orm import Session
from starlette import status


from app.security import create_access_token, get_hash
from app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES
from app.api.dependency import get_db, auth_user
from app.schemas.user import UserLogin, ResetPasswordForm
from app.crud import user as crud_user
from app.crud import password as crud_password

router = APIRouter()


"""
TODO
implement a max no of login trials before login gets blocked
"""


@router.post("/register")
def register(
    cred: UserLogin, 
    db: Session = Depends(get_db)
)-> Dict[str, Any]:

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
    pwd = get_hash(cred.master_pwd)  # hash once in the server
    # hash of the hash stored in db
    try:
        result = crud_user.post_user(db, email=cred.email, password=pwd)
    except IntegrityError as e:
        if (isinstance(e.orig, UniqueViolation)):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="email already exists")

    return result.dict(exclude_unset=True)


@router.post("/login")
def login(cred: UserLogin, response: Response, db: Session = Depends(get_db)):

    """
    ## API Login

    post user credentials (email & master password) to log in.
    The master password is hashed once in the server using bcrypt
    and upon insertion, it is hashed again at the postgres db
    using md5 by the pgcrypto extension.

    generates an access token upon login and sets response cookie

    """
    user_email = cred.email
    user_pass = cred.master_pwd

    password = get_hash(user_pass)
    if (res := crud_user.get_user_by_email(db, cred.email)) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="email not found"
        )

    if (user := crud_user.get_user(db, email=user_email, password=password)) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="invalid email/password"
        )

    # token expires after X minutes
    time_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = { "user_info": user.dict(exclude_unset=True) }

    access_token = create_access_token(data=payload, expires_delta=time_expires)

    # response = JSONResponse(content=payload)
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        max_age=time_expires.total_seconds(),
        expires=time_expires.total_seconds(),
        samesite='lax',
        secure=False
    )
    
    return payload


@router.get("/user")
def get_user_info(
    user=Depends(auth_user), 
    db: Session = Depends(get_db)
)-> Dict[str, Any]:
    return user.dict(exclude={"master_pwd"})




# @router.post("/reset_password")
# def reset_master_password(
#     credential: ResetPasswordForm,
#     db: Session = Depends(get_db),
# ):

#     if (user := crud_user.get_user_by_email(db, credential.email)) is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail="email not found"
#         )

#     # get the old password from the id
#     user_info = crud_user.get_user_by_id(db, user.id)
#     old_master_pwd = user_info.master_pwd

#     # update the master password entry
#     pwd = get_hash(credential.new_password)
#     updated_user = crud_user.update_user(
#         db, id=str(user.id), email=user.email, new_password=pwd
#     )

#     new_master_pwd = updated_user.master_pwd

#     # update all stored passwords with the new encryption
#     return crud_password.reset_pwd_all(
#         db,
#         old_master_pwd=old_master_pwd,
#         new_master_pwd=new_master_pwd,
#         user_id=str(user.id),
#     )
