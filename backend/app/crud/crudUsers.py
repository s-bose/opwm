from sqlalchemy.orm import Session
from pydantic import EmailStr

from app.models import User


def get_user_by_id(db: Session, id: str):
    """
    Fetches user information from the `User` table by
    querying by their id (uuid primary key)

    ### Only used internally via API dependencies

    Parameters
    ----------

    id  : uuid primary key, represented as str

    Returns
    -------

    sqlalchemy Row object
        <id, email, master_pwd>
    """

    query = f"""
    SELECT * FROM users WHERE id='{id}';
    """
    if (res := db.execute(query).fetchone()) is None:
        return None
    db.commit()
    return res


def get_user_by_email(db: Session, email: EmailStr):

    """
    Fetches user information from the `User` table by querying
    by their registered email address.

    ### Only used internally via API dependencies

    Parameters
    ----------

    email   : email used when registering

    Returns
    -------

    sqlalchemy Row object
        <id>
    """
    query = f"""
    SELECT id FROM users WHERE email='{email}';
    """
    if (id_ := db.execute(query).fetchone()) is None:
        return None
    db.commit()
    return id_


def get_user(db: Session, email: str, password: str) -> User:

    """
    Fetches user information from the `User` table by querying
    against email address and verifying the password.

    postgres `crypt()` function is used to verify the plaintext
    password with the stored hash.
    Returns a valid Row object only if the passwords match.
    otherwise returns None.

    ### Used for authenticating a user's account

    Parameters
    ----------

    email    : email credentials
    password : password credentials

    Returns
    -------

    sqlalchemy Row object
        <id, email>
    """
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


def post_user(db: Session, email: str, password: str) -> User:

    """
    Inserts a newly registered user's email and their hashed
    master password in the `Users` table.

    Uses the postgres `crypt()` function with salt to generate
    and store hashes of passwords.
    `Blowfish (bf)` hashing algorithm with 8 iterations is used here.

    ### Used for securely registering a new user's account

    Parameters
    ----------

    email    : email credentials
    password : password credentials

    Returns
    -------

    sqlalchemy Row object
        <id>
    """

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


def put_user(db: Session, email: str, new_passwd: str):
    pass
