import uuid
from sqlalchemy import Column, String
from sqlalchemy.sql.expression import text
from sqlalchemy_utils.types.uuid import UUIDType
from app.db import Base


class User(Base):
    __tablename__ = "users"
    # TODO - no autoincrement primary key
    id = Column(UUIDType, primary_key=True, unique=True,
                server_default=text("gen_random_uuid()"))
    email = Column(String, unique=True, nullable=False)
    master_pwd = Column(String, nullable=False)
