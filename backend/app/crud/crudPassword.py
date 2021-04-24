from sqlalchemy.orm import Session


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

    query = f"""
    INSERT INTO
        passwords(site, user_id, username, pwd) 
    VALUES (
        :site, 
        :user_id, 
        pgp_sym_encrypt(:username, :master_pwd),
        pgp_sym_encrypt(:password, :master_pwd))
    RETURNING id, site;
    """
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
    query = f"""
    SELECT
        site,
        pgp_sym_decrypt(username::bytea, :master_pwd) as username, 
        pgp_sym_decrypt(pwd::bytea, :master_pwd) as pwd
    FROM
        passwords
    WHERE
        user_id=:user_id;
    """
    pwd_list = db.execute(
        query, {"user_id": user_id, "master_pwd": master_pwd}
    ).fetchall()
    db.commit()
    return pwd_list


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

    query = f"""
    SELECT
        site,
        pgp_sym_decrypt(username::bytea, :master_pwd) as username, 
        pgp_sym_decrypt(pwd::bytea, :master_pwd) as pwd
    FROM 
        passwords 
    WHERE 
        user_id=:user_id AND 
        site=:site;
    """
    res = db.execute(
        query, {"site": site, "user_id": user_id, "master_pwd": master_pwd}
    ).fetchone()
    db.commit()
    return res
