from typing import Generator
from fastapi import Depends
from sqlalchemy.orm import Session

from app.db import SessionLocal


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def active_user(
    db: Session = Depends(get_db),
    *,
    user_id: int
):

    pass
