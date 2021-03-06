# fetch password factory
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

# fetch all passwords for a `user_id`
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

# post new password for a `user_id`
# returns inserted entry or none
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
    pid;
"""

# update an existing password for a `user_id`
# `COALESCE` retains prev value if `NULL` is passed
# NOTE - `NULL` does not equal empty strings
# returns updated entry or none 
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
    pid;
"""

# deletes a password for a given `user_id`
# returns deleted `pid`
delete_pwd_sql = """
DELETE FROM passwords
WHERE 
    user_id::text = :user_id AND
    pid::text = :pid
RETURNING
    pid;
"""

# bulk resets passwords 
# first decrypts them using `old_master_pwd`
# then hashes the `new_pwd` in db
# uses the hashed new_pwd as new master password
# to encrypt the decrypted passwords
# returning their `pid`s
reset_pwd_all_sql = """
WITH t AS (
	UPDATE users 
	SET
		master_pwd = crypt(:new_pwd, gen_salt('bf', 8))
	WHERE uid::text = :user_id
	RETURNING *
)
UPDATE passwords
	SET password=PGP_SYM_ENCRYPT(old_passwords.password, updated_user.master_pwd)
	FROM (SELECT * FROM t) updated_user, 
	(
		SELECT PGP_SYM_DECRYPT(password::bytea, :old_master_pwd) as password
		FROM passwords
		WHERE user_id::text = :user_id
	) old_passwords
    WHERE user_id::text = :user_id
RETURNING pid;

-- params - user_id         (user id UUID string)
-- params - new_pwd         (new password, hashed once)   
-- params - old_master_pwd  (old password, hashed twice)
"""

