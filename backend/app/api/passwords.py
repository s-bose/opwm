from typing import Any, Dict, List, Optional
from fastapi import APIRouter, Depends, HTTPException
from psycopg2.errors import UniqueViolation

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from starlette import status

from app import utils
from app.models import User
from app.schemas.user import UserBase
from app.api.dependency import auth_user, get_db
from app.schemas.passwords import PasswordInsert, PasswordUpdate, PasswordBase
from app.crud import password

router = APIRouter()


@router.get("/")
def get_password(
    site: str, user: UserBase = Depends(auth_user), db: Session = Depends(get_db)
) -> Dict[str, Any]:
    """
    retrieves the stored pwd for site for a given user
    (authenticated)
    """
    if (
        item := password.get_pwd(
            db, site=site, user_id=user.uid, master_pwd=user.master_pwd
        )
    ) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Password not found"
        )

    return item.dict(exclude_unset=True)


@router.get("/all")
def get_all_password(
    user: UserBase = Depends(auth_user), db: Session = Depends(get_db)
) -> List[Dict[str, Any]]:
    """
    retrieves all pwd for the logged in user
    """
    if (
        res_list := password.get_pwd_all(
            db, user_id=user.uid, master_pwd=user.master_pwd
        )
    ) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Password not found"
        )

    return [item.dict(exclude_unset=True) for item in res_list]


@router.post("/")
def post_password(
    cred: PasswordInsert,
    user: User = Depends(auth_user),
    db: Session = Depends(get_db),
) -> Dict[str, Any]:
    """
    stores a user-defined username/pwd for a site in vault
    (authenticated)
    """
    try:
        post_item = password.post_pwd(
            db, user_id=user.uid, master_pwd=user.master_pwd, **cred.dict()
        )
    except IntegrityError as e:
        print(e.orig)
        if isinstance(e.orig, UniqueViolation):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Error: entry already exists",
            )
    return post_item.dict(exclude_unset=True)


@router.put("/{pid}")
def update_password(
    pid: str,
    cred: PasswordUpdate,
    user: User = Depends(auth_user),
    db: Session = Depends(get_db),
) -> Dict[str, Any]:
    """
    changes the pwd for a site
    (authenticated)
    """

    if (
        update_item := password.update_pwd(
            db, pid=pid, user_id=user.uid, master_pwd=user.master_pwd, **cred.dict()
        )
    ) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="password not found"
        )

    return update_item.dict(exclude_unset=True)


@router.delete("/{pid}")
def delete_password(
    pid: str, user: User = Depends(auth_user), db: Session = Depends(get_db)
) -> PasswordBase:

    if (del_item := password.delete_pwd(db, user_id=user.uid, pid=pid)) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="password not found"
        )

    return {"deleted": True, **del_item.dict(exclude_unset=True)}


# @router.post("/")
# def reset_password(

# ):
# @router.get("/generate")
# def generate_pwd(
#     size: Optional[int] = None, urlsafe: bool = False, user: User = Depends(auth_user)
# ):
#     """
#     generates a random pwd and stores it wrt the username and site
#     (authenticated)
#     returns the random password
#     """

#     return {"password": utils.gen_random_pwd(size, urlsafe)}


# @router.post("/generate_kw")
# def generate_kw_pwd(
#     size: int, keyword: list, include_char: list, user: User = Depends(auth_user)
# ):
#     """
#     generates a pwd based on the list of keywords specified
#     everything else same as /generate
#     (authenticated)
#     """

#     return {"password": utils.gen_kw_pwd(keyword, size, include_char)}
