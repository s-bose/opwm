
from typing import Any, Dict, Optional
from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext

from fastapi.responses import JSONResponse


from app.core.config import SECRET_KEY, ALGORITHM

pwd_context = CryptContext(
    schemes=["bcrypt"], bcrypt__default_rounds=10, deprecated="auto")


def get_hash(password):
    return pwd_context.hash(password, salt=SECRET_KEY[:21] + '.')


def create_access_token(
    data: Dict[str, Any],
    expires_delta: Optional[timedelta] = None
):

    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
