from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import create_database, database_exists
from app.core.config import DATABASE_URL

if not database_exists(DATABASE_URL):
    create_database(DATABASE_URL)
engine = create_engine(DATABASE_URL, echo=True)  # database engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()  # sqlalchemy Base class
