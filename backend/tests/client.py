from fastapi import Request

from fastapi.testclient import TestClient

from app.api.dependency import auth_user, get_db
from app.schemas.user import UserBase

from app.main import app

from .conftest import TEST_USER





def temp_db(f):
    def func(SessionLocal, *args, **kwags):
        def override_get_db():
            db = SessionLocal()
            try:
                yield db
            finally:
                db.close()

        def override_auth_user(request: Request):
            return UserBase(**TEST_USER)

        app.dependency_overrides[get_db] = override_get_db
        app.dependency_overrides[auth_user] = override_auth_user
        f(*args, **kwags)
        app.dependency_overrides[get_db] = get_db
        app.dependency_overrides[auth_user] = auth_user
    
    return func

client = TestClient(app)
