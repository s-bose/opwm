from fastapi import FastAPI
from databases import Database

from app.core.config import DATABASE_URL

db = Database(DATABASE_URL)
