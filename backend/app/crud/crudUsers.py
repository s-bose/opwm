from sqlalchemy.orm import Session
from pydantic import EmailStr

from app.models import User


def get_user_by_id(
    db: Session,
    id: int
):
    query = f"""
    SELECT * FROM users WHERE id={id};
    """
    if (res := db.execute(query).fetchone()) is None:
        return None
    db.commit()
    return res


def get_user_by_email(
    db: Session,
    email: EmailStr
):
    query = f"""
    SELECT id FROM users WHERE email='{email}';
    """
    if (id_ := db.execute(query).fetchone()) is None:
        return None
    db.commit()
    return id_


def get_user(
    db: Session,
    email: str,
    password: str
) -> User:

    query = f"""
    SELECT id, email
    FROM 
        users 
    WHERE
        email='{email}' AND
        master_pwd=crypt('{password}', master_pwd);
    """
    if (res := db.execute(query).fetchone()) is None:
        return None
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
        ('{email}', crypt('{password}', gen_salt('bf', 8)))
    RETURNING id;
    """

    res = db.execute(query).fetchone()
    db.commit()
    return res


def put_user(
    db: Session,
    email: str,
    new_passwd: str
):
    pass
