

from sqlalchemy.orm import Session

from app.crud.crudBase import execute_query
from app.models import User


def get_active_user(
    db: Session,
    user_id: int
):
    query = f"""SELECT id FROM users WHERE id={user_id};"""
    res = execute_query(db, query)
    return {
        "id": res[0]
    }


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
        master_pwd=crypt('{password}', master_pwd);
    """
    res = execute_query(db, query)
    user = User(**res)
    db.commit()
    return user


def post_user(
    db: Session,
    email: str,
    password: str
) -> User:

    query = f"""
    INSERT INTO 
        users(email, master_pwd)
    VALUES 
        ('{email}', crypt('{password}', gen_salt('md5')));
    """

    res = execute_query(db, query)
    user = User(**res)
    db.commit()
    return user


def put_user(
    db: Session,
    email: str,
    new_passwd: str
):
    pass
