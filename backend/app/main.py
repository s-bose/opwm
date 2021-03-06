from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette import status
from app.api import router as main_router
from sqlalchemy.exc import IntegrityError

from starlette.responses import Response

from psycopg2.errors import UniqueViolation

description="""
Offline Password Manager is a fully-offline application for storing
and managing passwords from various websites and applications.
"""

app = FastAPI(
    title="OPWM",
    description=description
)

# allow CORS requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3333", "http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(main_router, prefix="/api")

# handle any uncaught DB-API exception (IntegrityError)
@app.exception_handler(IntegrityError)
def db_exc_handler(req: Request, exc: IntegrityError):
    if isinstance(exc.orig, UniqueViolation):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"info": "Database Operation Error", "detail": str(exc).split(" ")[0]},
        )





