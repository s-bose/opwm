from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from starlette.middleware.cors import CORSMiddleware

from app.api import router as main_router

app = FastAPI()

app.include_router(main_router, prefix="/api")
