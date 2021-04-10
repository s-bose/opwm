from sqlalchemy.orm import Session


def execute_query(
    db: Session,
    query: str
):

    res = db.execute(query)
    db.commit()
    return res

# TODO exception handling


