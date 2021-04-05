from sqlalchemy.orm import Session


def execute_query(
    db: Session,
    query: str
) -> tuple:

    res = db.execute(query).fetchone()
    db.commit()
    return res

# TODO exception handling
