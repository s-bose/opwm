# example pytest conftest w alembic integration
# https://github.com/nikaera/fastapi-sqlalchemy-alembic-pytest-sample


import os
import alembic.config
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database, drop_database

from app.core.config import DATABASE_URL
from app.security import create_access_token

from sqlalchemy.ext.declarative import declarative_base

# test user config
TEST_USER = {
    "uid": "4288921a-f7ba-4c83-969f-54f30be4ee5f",
    "email": "john@doe.com", 
    "master_pwd": "password"
}

TEST_ACCESS_TOKEN = create_access_token(data=TEST_USER, expires_delta=None)

TEST_SQL = """
INSERT INTO 
    users 
VALUES (:uid, :email, crypt(:master_pwd, gen_salt('bf', 8)))
RETURNING uid;
"""

TEST_DB_URL = f"{DATABASE_URL}_test"


# run online migration through connection
def alembic_migration(migrations_path: str,  alembic_init_path: str = 'alembic.ini', connection = None, revision: str = 'head'):
    config = alembic.config.Config(alembic_init_path)
    config.set_main_option('script_location', migrations_path)      
    if connection is not None:
        config.attributes['connection'] = connection
    alembic.command.upgrade(config, revision)


# session fixture
@pytest.fixture(scope='session', autouse=True)
def SessionLocal():
    os.environ['TEST'] = "1"
    engine = create_engine(TEST_DB_URL)

    # assert not database_exists(TEST_DB_URL)
    if database_exists(TEST_DB_URL):
        drop_database(TEST_DB_URL)

    create_database(TEST_DB_URL)

    with engine.begin() as conn:
        print("creating tables")
        
        alembic_migration(migrations_path="alembic",  alembic_init_path="alembic.ini", connection=conn)
    
    Base = declarative_base()
    Base.metadata.create_all(engine)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()
    session.execute(TEST_SQL, TEST_USER)
    session.commit()
    yield SessionLocal

    drop_database(TEST_DB_URL)
    engine.dispose()
    del os.environ["TEST"]


