from typing import Any, Dict
from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, Response
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError

from sqlalchemy.orm import Session
from starlette import status


from app.security import create_access_token, get_hash
from app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES
from app.api.dependency import get_db, auth_user
from app.schemas.user import UserBase, UserLogin, ResetPasswordForm
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
) -> Dict[str, Any]:

    """
    ## API Register

    Registers a new user into the system by storing their email &
    master password (hash) in the database

    Master password is first hashed once at the API then again in the
    db using pgcrypto.

    Parameters
    ----------

    email: EmailStr
    master_pwd: tr

    Returns
    -------

    Dict[str, Any]
    """

    pwd = get_hash(cred.master_pwd)  # hash once in the server
   

    try:                             # hash of the hash stored in db
        result: UserBase = crud_user.post_user(db, email=cred.email, password=pwd)
    except IntegrityError as e:
        if isinstance(e.orig, UniqueViolation):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="email already exists"
            )

    return result.dict(exclude_unset=True)


@router.post("/login")
def login(
    cred: UserLogin, 
    response: Response, 
    db: Session = Depends(get_db)
):

    """
    ## API Login

    post user email & master password to log in.

    Master password is hashed once in the server using bcrypt then
    hashed and checked at db using pgcrypto extension.

    generates an access token upon login and sets response cookie
    
    Parameters
    ----------
    email: EmailStr
    master_pwd: tr

    Returns
    -------
    fastapi.Response
    """
    user_email = cred.email
    user_pass = cred.master_pwd

    password = get_hash(user_pass)

    # check if user with this email exists
    if (res := crud_user.get_user_by_email(db, cred.email)) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="email not found"
        )

    # authentication check
    if (user := crud_user.get_user(db, email=user_email, password=password)) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="invalid email/password"
        )

    # generate payload and access token
    time_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = { "user_info": user.dict(exclude_unset=True) }

    access_token = create_access_token(data=payload, expires_delta=time_expires)

    # set cookie
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        max_age=time_expires.total_seconds(),
        expires=time_expires.total_seconds(),
        samesite="lax",
        secure=False,
    )

    return payload

### AUTHENTICATED 
@router.get("/user")
def get_user_info(
    user: UserBase = Depends(auth_user), 
    db: Session = Depends(get_db)
) -> Dict[str, Any]:

    """
    ## API Get User

    Retrieve the currently logged in user information
    
    Parameters
    ----------
    None
    
    Returns
    --------
    user_id : UUID
    email   : EmailStr
    """
    return user.dict(exclude={"master_pwd"})



@router.delete("/user")
def delete_user(
    user: UserBase = Depends(auth_user), 
    db: Session = Depends(get_db)
)-> Dict[str, Any]:

    """
    deletes the currently logged in user

    Parameters
    ----------
    None
    
    Returns
    --------
    user_id : UUID
    """
    return crud_user.delete_user(user.uid).dict(exclude_unset=True)

# # TODO - NOT DONE
# @router.post("/reset_password")
# def reset_master_password(
#     credential: ResetPasswordForm,
#     db: Session = Depends(get_db),
# ):
#     """
#     Not authenticated.

#     The same function can be used for `forgot password` at Login
#     or, after login for manually resetting password

#     """
#     # TODO -implement this
#     if (user := crud_user.get_user_by_email(db, credential.email)) is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, 
#             detail="email not found"
#         )

#     # get the old password from the id
#     user_info = crud_user.get_user_by_id(db, user.uid)
#     old_master_pwd = user_info.master_pwd

#     # update the master password entry
#     new_master_pwd = get_hash(credential.new_password)
#     updated_user = crud_user.update_user(
#         db, _id=user.uid, email=user.email, new_password=new_master_pwd
#     )

#     new_master_pwd = crud_user.get_user_by_id(db, user_id)

#     # update all stored passwords with the new encryption
#     return crud_password.reset_pwd_all(
#         db,
#         old_master_pwd=old_master_pwd,
#         new_master_pwd=new_master_pwd,
#         user_id=str(user.id),
#     )
