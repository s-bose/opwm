from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm
)

from pydantic import EmailStr

from sqlalchemy.orm import Session

from starlette import status

from app.crud.usersCrud import get_user
from app.api.dependency import get_db

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


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")


# # @router.post("/login")
# # async def login(
# #     db: Session = Depends(get_db),
# #     form_data: OAuth2PasswordRequestForm = Depends()
# # ) -> None:
# #     """
# #     logs in
# #     """
# #     user_email = form_data.username
# #     user_pass = form_data.password
# #     if (user := get_user(db, user_email, user_pass)) is None:
# #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
# #                             detail="wrong username/password")
# #     return {'access-token': form_data.username}


# @router.put("/user")
# def user() -> None:
#     return None

@router.post('/login')
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # user_dict = fake_users_db.get(form_data.username)
    # if not user_dict:
    #     raise HTTPException(status_code=400, detail="Incorrect username or password")
    # user = UserInDB(**user_dict)
    # hashed_password = fake_hash_password(form_data.password)
    # if not hashed_password == user.hashed_password:
    # raise HTTPException(status_code=400, detail="Incorrect username or password")
    #
    return {"access_token": form_data.username, "token_type": "bearer"}


@router.get('/test')
def test(token: str = Depends(oauth2_scheme)):
    return {'token': token}
# @router.post("/reset_pwd")
# def reset_master_pwd() -> None:
#     return None
