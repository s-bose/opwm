get_pwd_sql = """
SELECT
    site,
    pgp_sym_decrypt(username::bytea, :master_pwd) as username, 
    pgp_sym_decrypt(pwd::bytea, :master_pwd) as pwd
FROM 
    passwords 
WHERE 
    user_id::text=:user_id AND 
    site=:site;
"""

get_pwd_all_sql = """
SELECT
    site,
    pgp_sym_decrypt(username::bytea, :master_pwd) as username, 
    pgp_sym_decrypt(pwd::bytea, :master_pwd) as pwd
FROM
    passwords
WHERE
    user_id::text=:user_id;
"""

post_pwd_sql = """
INSERT INTO
    passwords(site, user_id, username, pwd) 
VALUES (
    :site, 
    :user_id, 
    pgp_sym_encrypt(:username, :master_pwd),
    pgp_sym_encrypt(:password, :master_pwd))
RETURNING id, site;
"""

update_pwd_sql = """
UPDATE passwords
SET 
    site=:site,
    username = pgp_sym_encrypt(:username, :master_pwd),
    password = pgp_sym_encrypt(:password, :master_pwd)
WHERE user_id::text:user_id;
RETURNING id, site;
"""