from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import user
from app.models import Passwords


def get_pwd_all(
    db: Session,
    user_id: int,
    master_pwd: str
):
    query = f"""
    SELECT
        site,
        pgp_sym_decrypt(username::bytea, '{master_pwd}') as username, 
        pgp_sym_decrypt(pwd::bytea, '{master_pwd}') as pwd
    FROM
        passwords
    WHERE
        user_id={user_id};
    """
    pwd_list = db.execute(query).fetchall()
    db.commit()
    return pwd_list


def get_pwd(
    db: Session,
    site: str,
    user_id: int,
    master_pwd: str
):

    query = f"""
    SELECT
        site,
        pgp_sym_decrypt(username::bytea, '{master_pwd}') as username, 
        pgp_sym_decrypt(pwd::bytea, '{master_pwd}') as pwd
    FROM 
        passwords 
    WHERE 
        user_id={user_id} AND 
        site='{site}';
    """
    res = db.execute(query).fetchone()
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
        pgp_sym_encrypt('{username}', '{master_pwd}'),
        pgp_sym_encrypt('{password}', '{master_pwd}'))
    RETURNING id, site;
    """
    res = db.execute(query).fetchone()
    db.commit()
    return res
