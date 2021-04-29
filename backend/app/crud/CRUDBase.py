from typing import Dict, Any
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from sqlalchemy.exc import IntegrityError

def query_execute(
    db: Session,
    query: str,
    params: Dict[str, Any],
):
    query = text(query)
    try:
        result = db.execute(query, params)
        db.commit()
        return result
    except IntegrityError as e:
        db.rollback()
        raise e




