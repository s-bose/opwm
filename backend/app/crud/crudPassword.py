from sqlalchemy.orm import Session
from app.models import Passwords


def get_pwd(
    db: Session,
    site: str,
    user_id: int,
    master_pwd: str
):

    query = f"""
    SELECT
        username, 
        pgp_sym_decrypt(pwd::bytea, '{master_pwd}') as pwd
    FROM 
        passwords 
    WHERE 
        user_id={user_id} AND 
        site='{site}';
    RETURNING site, username, pwd;
    """
    res = db.execute(query).fetchone()[0]
    db.commit()
    return res


def post_pwd(
    db: Session,
    site: str,
    user_id: int,
    username: str,
    password: str,
    master_pwd: str
):
    query = f"""
    INSERT INTO
        passwords(site, user_id, username, pwd) 
    VALUES (
        '{site}', 
        {user_id}, 
        '{username}', 
        pgp_sym_encrypt('{password}', '{master_pwd}'))
    RETURNING id, site, username;
    """
    res = db.execute(query).fetchone()[0]
    db.commit()
    return res
