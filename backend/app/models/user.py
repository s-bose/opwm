import uuid
from sqlalchemy import Column, String
from sqlalchemy.sql.expression import text
from sqlalchemy_utils.types.uuid import UUIDType
from app.db import Base


class User(Base):
    """
    ## User table

    This table is used to store the credentials for the users
    of the password manager.
    It only stores the email and master password (hashed) for
    registration & login and for password generation / storage
    in the vault.

    id column is primary key but instead of autoincrementing
    integers, we use UUID which is slower but safer and
    generates a unique key for each new user.

    This again utilises the `gen_random_uuid()` function
    from the pgcrypto extension at the database side to generate
    the UUIDs for us.

    """

    __tablename__ = "users"

    id = Column(
        UUIDType,
        primary_key=True,
        unique=True,
        server_default=text("gen_random_uuid()"),
    )
    email = Column(String, unique=True, nullable=False)
    master_pwd = Column(String, nullable=False)
    recovery_email = Column(String, unique=True, nullable=True)
