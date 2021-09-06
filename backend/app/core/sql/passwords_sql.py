get_pwd_sql = """
SELECT
    pid,
    site,
    link,
    username, 
    pgp_sym_decrypt(password::bytea, :master_pwd) as password
FROM 
    passwords 
WHERE 
    user_id::text = :user_id AND 
    site = :site;
"""

get_pwd_all_sql = """
SELECT
    pid,
    site,
    link,
    user_id,
    username, 
    pgp_sym_decrypt(password::bytea, :master_pwd) as password
FROM
    passwords
WHERE
    user_id::text = :user_id;
"""

post_pwd_sql = """
INSERT INTO
    passwords(site, link, user_id, username, password) 
VALUES (
    :site,
    :link, 
    :user_id, 
    :username,
    pgp_sym_encrypt(:password, :master_pwd))
RETURNING 
    pid,
    site,
    link,
    username, 
    pgp_sym_decrypt(password::bytea, :master_pwd) as password;
"""

update_pwd_sql = """
UPDATE passwords
SET 
    site = COALESCE(:new_site, site),
    link = COALESCE(:new_link, link),
    username = COALESCE(:new_username, username),
    password = COALESCE(pgp_sym_encrypt(:new_password, :master_pwd), password::bytea)
WHERE 
    user_id::text = :user_id AND
    pid::text = :pid
RETURNING 
    pid, 
    site,
    link,
    username,
    pgp_sym_decrypt(password::bytea, :master_pwd) as password;
"""

delete_pwd_sql = """
DELETE FROM passwords
WHERE 
    user_id::text = :user_id AND
    pid::text = :pid
RETURNING
    pid;
"""


reset_pwd_all_sql = """
UPDATE passwords
SET username = pgp_sym_encrypt(t.username, :new_master_pwd),
password = pgp_sym_encrypt(t.password, :new_master_pwd)
FROM
(SELECT
	pgp_sym_decrypt(username::bytea, :old_master_pwd) as username,
	pgp_sym_decrypt(password::bytea, :old_master_pwd) as password
FROM passwords
WHERE user_id = :user_id)
RETURNING pid, site;
"""
