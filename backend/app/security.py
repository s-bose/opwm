from typing import Any, Dict, Optional
from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from pydantic import EmailStr

from app.core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

pwd_context = (
    CryptContext(  # a CryptContext instance using bcrypt function with 10 rounds
        schemes=["bcrypt"], bcrypt__default_rounds=10, deprecated="auto"
    )
)


def get_hash(password):
    """
    since bcrypt uses salt size of 22 chars only, and we need a constant salt
    because otherwise we will end up with different hashes each time for the same
    plaintext.
    Hence, we use the first 21 chars of the SECRET_KEY env var, with a `.` (dot)
    at the end, since the salt pattern for bcrypt needs a dot in the end
    """
    return pwd_context.hash(password, salt=SECRET_KEY[:21] + ".")


def create_access_token(
    data: Dict[str, Any], expires_delta: Optional[timedelta] = None
):

    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# TODO - recovery password is difficult as it requires an smtp server or a personal mail account credentials
# def generate_password_reset_token(email: EmailStr) -> str:
#     expires = datetime.utcnow() + timedelta(minutes=PWD_RESET_TOKEN_EXPIRE_MINUTES)
#     exp = expires.timestamp()
#     encoded_jwt = jwt.encode(
#         {"exp": exp, "email": email},
#         SECRET_KEY,
#         algorithm=ALGORITHM,
#     )
#     return encoded_jwt


# def send_reset_password_email(email: EmailStr, token: str):

#     server_host = "http://localhost:8000"
#     message = emails.Message(
#         subject=f"Password reset request for {email}",
#         body=f"{server_host}/reset-password?token={token}",
#         mail_from=("user", email)
#     )

#     response = message.send(to=email)
