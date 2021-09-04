from typing import Any, Dict, List, Optional
from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from starlette import status

from app import utils
from app.models import User
from app.schemas.user import UserBase
from app.api.dependency import auth_user, get_db
from app.schemas.passwords import PasswordInsert
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
        res := password.get_pwd(
            db, site=site, user_id=user.uid, master_pwd=user.master_pwd
        )
    ) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Password not found"
        )

    return res.dict(exclude_unset=True)


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
) -> None:
    """
    stores a user-defined username/pwd for a site in vault
    (authenticated)
    """
    pwd_insert = cred.dict(exclude_unset=True)

    return password.post_pwd(
        db, user_id=user.uid, master_pwd=user.master_pwd, **pwd_insert
    ).dict(exclude_unset=True)


@router.put("/")
def update_password(
    cred: PasswordInsert, user: User = Depends(auth_user), db: Session = Depends(get_db)
) -> None:
    """
    changes the pwd for a site
    (authenticated)
    """

    pass
    # pwd_update = cred.dict(exclude_unset=True)

    # return None


@router.get("/generate")
def generate_pwd(
    size: Optional[int] = None, urlsafe: bool = False, user: User = Depends(auth_user)
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
