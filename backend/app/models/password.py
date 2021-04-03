from app.db import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class Passwords(Base):
    __tablename__ = "passwords"
    id = Column(Integer, primary_key=True, autoincrement=True)
    site = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    username = Column(String, nullable=False)
    pwd = Column(String, nullable=False, unique=True)
