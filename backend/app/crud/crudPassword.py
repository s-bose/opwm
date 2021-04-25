from sqlalchemy.orm import Session
from sqlalchemy.sql import text

import app.core.sql.passwords_sql as sql


def get_pwd(db: Session, site: str, user_id: str, master_pwd: str):
    """
    Retrieves a single stored credential for a given `site`
    against the logged in user.

    The stored encrypted username & password is decrypted
    with `PGP_SYM_DECRYPT` using the hash of the user's master
    password.

    Parameters
    ----------

    site       : name of the site
    user_id    : uuid of the logged in user
    master_pwd : stored hash of the user's master password

    Returns
    -------

    site       : name of the site
    username   : decrypted plaintext username
    password   : decrypted plaintext username
    """

    query = text(sql.get_pwd_sql)

    res = db.execute(
        query, {"site": site, "user_id": user_id, "master_pwd": master_pwd}
    ).fetchone()
    db.commit()
    return res


def get_pwd_all(db: Session, user_id: str, master_pwd: str):
    """
    Retrieves all the stored credentials for the logged in user.

    Parameters
    ----------

    user_id    : uuid of the logged in user
    master_pwd : stored hash of the user's master password

    Returns
    -------

    list
        a list of dicts containing the following

        site       : name of the site
        username   : decrypted plaintext username
        password   : decrypted plaintext username
    """
    query = text(sql.get_pwd_all_sql)

    pwd_list = db.execute(
        query, {"user_id": user_id, "master_pwd": master_pwd}
    ).fetchall()
    db.commit()
    return pwd_list


def post_pwd(
    db: Session, site: str, user_id: str, username: str, password: str, master_pwd: str
):
    """
    Inserts one `<username, password>` credential pair for a given `site`
    against the logged in user.

    Both the username and password is encrypted with `PGP_SYM_ENCRYPT`
    using the stored hash of the user's master password

    Parameters
    ----------

    site       : name of the site
    user_id    : uuid of the logged in user
    username   : username credentials
    password   : password credentials
    master_pwd : stored hash of the user's master password

    Returns
    -------

    sqlalchemy Row object
        <id, site>
    """

    query = text(sql.post_pwd_sql)

    res = db.execute(
        query,
        {
            "site": site,
            "user_id": user_id,
            "username": username,
            "password": password,
            "master_pwd": master_pwd,
        },
    ).fetchone()
    db.commit()
    return res


def update_pwd(
    db: Session,
    site: str,
    user_id: str,
    new_username: str,
    new_password: str,
    master_pwd: str,
):

    """
    updates a single username/password entry for a given `site`

    """

    query = text(sql.update_pwd_sql)

    res = db.execute(
        query,
        {
            "site": site,
            "user_id": user_id,
            "username": new_username,
            "password": new_password,
            "master_pwd": master_pwd,
        },
    ).fetchone()
    db.commit()
    return res


def reset_pwd_all(db: Session, old_master_pwd: str, new_master_pwd: str, user_id: str):

    query = text(sql.reset_pwd_all_sql)

    res = db.execute(
        query,
        {
            "old_master_pwd": old_master_pwd,
            "new_master_pwd": new_master_pwd,
            "user_id": user_id,
        },
    ).fetchall()
    db.commit()
    return res