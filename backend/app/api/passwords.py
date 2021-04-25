from typing import Any, Dict
from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session
from pydantic import SecretStr

from app import utils
from app.models import User
from app.api.dependency import auth_user, get_db
from app.crud.crudPassword import post_pwd, get_pwd, get_pwd_all
from app.schemas.passwords import PasswordInsert

router = APIRouter()


@router.get("/")
def get_password(
    site: str, user: User = Depends(auth_user), db: Session = Depends(get_db)
) -> Dict[str, Any]:
    """
    retrieves the stored pwd for site for a given user
    (authenticated)
    """
    return get_pwd(db, site=site, user_id=str(user.id), master_pwd=user.master_pwd)


@router.get("/all")
def get_all_password(user: User = Depends(auth_user), db: Session = Depends(get_db)):
    """
    retrieves all pwd for the logged in user
    """
    return get_pwd_all(db, user_id=str(user.id), master_pwd=user.master_pwd)


@router.post("/")
def post_password(
    # form_data: PasswordInsert = Depends(),
    cred: PasswordInsert,
    user: User = Depends(auth_user),
    db: Session = Depends(get_db),
) -> None:
    """
    stores a user-defined username/pwd for a site in vault
    (authenticated)
    """

    return post_pwd(
        db,
        site=cred.site,
        user_id=str(user.id),
        username=cred.username,
        password=cred.password,
        master_pwd=user.master_pwd,
    )


@router.put("/")
def change_password(
    site: str, username: str, new_pwd: str, user: User = Depends(auth_user)
) -> None:
    """
    changes the pwd for a site
    (authenticated)
    """
    return None


@router.get("/generate")
def generate_pwd(
    size: int = None, urlsafe: bool = False, user: User = Depends(auth_user)
):
    """
    generates a random pwd and stores it wrt the username and site
    (authenticated)
    returns the random password
    """

    return {"password": utils.gen_random_pwd(size, urlsafe)}


@router.post("/generate_kw")
def generate_kw_pwd(
    size: int, keyword: list, include_char: list, user: User = Depends(auth_user)
):
    """
    generates a pwd based on the list of keywords specified
    everything else same as /generate
    (authenticated)
    """

    return {"password": utils.gen_kw_pwd(keyword, size, include_char)}
