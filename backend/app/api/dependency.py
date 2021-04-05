from typing import Generator
from fastapi import Depends
from sqlalchemy.orm import Session

from app.db import SessionLocal
from app.crud.usersCrud import get_active_user


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
