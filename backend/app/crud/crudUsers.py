from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from pydantic import EmailStr
from typing import Dict

from app.schemas.user import UserBase

import app.core.sql.users_sql as sql


def get_user_by_id(db: Session, id: str) -> UserBase:
    """
    Fetches user information from the `User` table by
    querying by their id (uuid primary key)

    ### Only used internally via API dependencies

    Parameters
    ----------

    id  : uuid primary key, represented as str

    Returns
    -------

    UserBase model

    id         : uuid primary key, as str
    email      : user email
    master_pwd : master password (hash)

    """

    query = text(sql.get_user_by_id_sql)
    if (res := db.execute(query, {"id": id}).fetchone()) is None:
        return None
    db.commit()
    return UserBase(id=res.uid, email=res.email, master_pwd=res.master_pwd)


def get_user_by_email(db: Session, email: EmailStr) -> str:

    """
    Fetches user information from the `User` table by querying
    by their registered email address.

    ### Only used internally via API dependencies

    Parameters
    ----------

    email   : email used when registering

    Returns
    -------

    id  : uuid primary key, as str

    """
    query = text(sql.get_user_by_email_sql)
    if (res := db.execute(query, {"email": email}).fetchone()) is None:
        return None
    db.commit()
    return str(res.uid)


def get_user(db: Session, email: str, password: str) -> UserBase:

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

    UserBase model

    id    : uuid primary key, as str
    email : user email

    """
    query = text(sql.get_user_auth_sql)
    if (
        res := db.execute(query, {"email": email, "password": password}).fetchone()
    ) is None:
        return None
    db.commit()
    return UserBase(id=res.uid, email=res.email)


def post_user(db: Session, email: str, password: str) -> str:

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

    id : uuid primary key of inserted row, as str
    """

    query = text(sql.post_user_sql)

    res = db.execute(query, {"email": email, "password": password}).fetchone()
    db.commit()
    return str(res.uid)


def update_user(db: Session, id: str, email: str, new_password: str) -> UserBase:

    """
    Updates an existing user's credentials by changing
    the old master password hash with a new one.
    ###
    # This does not update the existing username/passwords
    # stored in the `Passwords` table
    # For that, an additional query on `Passwords` table
    # needs to be applied.

    Parameters
    ----------

    email        : user email
    new_password : (plaintext) new master password

    Returns
    -------

    UserBase model

    id    : uuid primary key of the updated row, as str
    email : user email

    """
    query = text(sql.update_user_sql)

    res = db.execute(
        query, {"email": email, "new_password": new_password, "id": id}
    ).fetchone()
    db.commit()
    return UserBase(id=res.uid, email=res.email)
