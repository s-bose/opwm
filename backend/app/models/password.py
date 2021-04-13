import uuid
from sqlalchemy import Column, String, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.sql.expression import text
from sqlalchemy_utils.types.uuid import UUIDType

from app.db import Base


class Passwords(Base):
    """
    ## Passwords table

    This table stores and manages all the `(username, password)`
    pairs a logged in user might want to store.

    The credentials are symmetrically encrypted with the stored
    hash of the master password for the user.

    Similar to User table, the id column here too is UUID for
    security concerns.


    """

    __tablename__ = "passwords"

    id = Column(
        UUIDType,
        primary_key=True,
        unique=True,
        server_default=text("gen_random_uuid()"),
    )
    site = Column(String, nullable=False)
    user_id = Column(UUIDType, ForeignKey("users.id"))
    username = Column(String, nullable=False)
    pwd = Column(String, nullable=False, unique=True)
