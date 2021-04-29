from typing import Dict, Any, Generic, TypeVar
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from sqlalchemy.exc import IntegrityError


SchemaType = TypeVar('SchemaType', bound=BaseModel)

class CRUDBase(Generic[SchemaType]):
    def __init__(self, schema: SchemaType):
        self.schema = schema
    

    def query_execute(
        self,
        db: Session,
        query: str,
        params: Dict[str, Any],
    ):
        query = text(query)
        try:
            result = db.execute(query, params).fetchone()
            db.commit()
            return self.schema(**result) if result else None
        except IntegrityError as e:
            db.rollback()
            raise e

    def query_execute_all(
        self,
        db: Session,
        query: str,
        params: Dict[str, Any],
    ):
        query = text(query)
        try:
            result = db.execute(query, params).fetchall()
            db.commit()
            return [self.schema(**item) for item in result] if result else None
        except IntegrityError as e:
            db.rollback()
            raise e




