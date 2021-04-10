

from sqlalchemy.orm import Session

from app.crud.crudBase import execute_query
from app.models import User

from app.api.dependency import get_db


def get_user(
    db: Session,
    email: str,
    password: str
) -> User:

    query = f"""
    SELECT * 
    FROM 
        users 
    WHERE
        email='{email}' AND
        master_pwd=crypt('{password}', master_pwd)
    RETURNING id, email;
    """
    res = db.execute(query).fetchone()[0]
    db.commit()
    return res


def post_user(
    db: Session,
    email: str,
    password: str
) -> User:

    query = f"""
    INSERT INTO 
        users(email, master_pwd)
    VALUES 
        ('{email}', crypt('{password}', gen_salt('md5')))
    RETURNING id;
    """

    res = db.execute(query).fetchone()[0]
    db.commit()
    return res


def put_user(
    db: Session,
    email: str,
    new_passwd: str
):
    pass
