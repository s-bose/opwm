from fastapi import FastAPI

from app.db import Base
from app.api import router as main_router
from app.db import engine
# TODO - this is bad, use alembic maybe?
from app.models import User, Passwords

from app.core.config import DATABASE_URL
app = FastAPI()

print(DATABASE_URL)
app.include_router(main_router, prefix="/api")

Base.metadata.create_all(bind=engine)
