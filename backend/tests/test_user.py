

import pytest
import alembic
from alembic.config import Config

from fastapi.testclient import TestClient
import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists, drop_database
from sqlalchemy.orm import sessionmaker
from starlette.datastructures import Headers



from app.core.config import DATABASE_URL


from app.main import app
from app.api.dependency import get_db

TEST_DB_URL = f"{DATABASE_URL}_test"



@pytest.fixture(scope='module', autouse=True)
def connection():
    print(TEST_DB_URL)
    if database_exists(TEST_DB_URL):
        drop_database(TEST_DB_URL)

    create_database(TEST_DB_URL)

    alembic_cfg = Config("alembic.ini")
    alembic_cfg.set_main_option('sqlalchemy.url', str(TEST_DB_URL))
    alembic.command.upgrade(alembic_cfg, "head")

    engine = create_engine(TEST_DB_URL)
    connection = engine.connect()
    yield connection
    connection.close()

@pytest.fixture(scope="module", autouse=True)
def session(connection):
    transaction = connection.begin()
    SessionLocalTest = sessionmaker(bind=connection)
    session = SessionLocalTest()
    yield session
    session.close()
    transaction.rollback()
    drop_database(TEST_DB_URL)

@pytest.fixture(scope="module")
def client(session):
    def override_get_db():
        yield session

    app.dependency_overrides[get_db] = override_get_db
    client = TestClient(app)
    yield client
    del app.dependency_overrides[get_db]


    

def test_user_register(client):
    response = client.post("/api/register", json={"email": "abc@abc.com", "master_pwd": "pass"})
    print(response)
    assert response.status_code == 200

access_token = ""

def test_user_login(client):
    response = client.post("/api/login", json={"email": "abc@abc.com", "master_pwd": "pass"})
    # access_token = response.json().get('access_token')
    assert response.status_code == 200

# def test_get_user(client):
#     response = client.get("/api/user", Headers={"access_token": access_token})
#     assert response.status_code == 200