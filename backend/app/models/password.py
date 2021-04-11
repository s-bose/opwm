from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    UniqueConstraint
)

from app.db import Base

class Passwords(Base):
    __tablename__ = "passwords"
    id = Column(Integer, primary_key=True, autoincrement=True) # TODO - no autoincrement pk
    site = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    username = Column(String, nullable=False)
    pwd = Column(String, nullable=False, unique=True)
    UniqueConstraint('site', 'user_id', name='uid_site_uniq')
