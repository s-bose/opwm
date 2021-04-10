from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)
from sqlalchemy.orm import Session
from starlette import status

from app.security import get_hash

from app.crud import crudUsers
from app.api.dependency import get_db

from app.schemas.user import UserModel
router = APIRouter()


# @router.post("/register")
# def register(
#     name: str,
#     email: EmailStr,
#     password: str
# ) -> None:
#     """
#     registers a user with email and master password
#     """
#     return None


# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")


"""
TODO 
hash master password twice. once at the register phase. then at the db

"""


@router.post("/register")
def register(
    cred: UserModel,
    db: Session = Depends(get_db)
):
    pwd = get_hash(cred.master_pwd)       # hash once in the server

    # hash of the hash stored in db
    _id = crudUsers.post_user(db, email=cred.email, password=pwd)

    return {
        "id": _id
    }


@router.post("/login")
def login(
    cred: UserModel,
    db: Session = Depends(get_db)
) -> None:
    """
    logs in
    """
    user_email = cred.email
    user_pass = cred.master_pwd
    if (user := crudUsers.get_user(db, user_email, user_pass)) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="wrong username/password")

    return {'access-token': user.id, 'token_type': 'bearer'}
