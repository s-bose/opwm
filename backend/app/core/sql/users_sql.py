
# fetch user factory
# returns all or none
get_user_by_id_sql = """
SELECT * FROM users WHERE uid::text = :id;
"""


# fetch user by email
# returns `uid` or none
get_user_by_email_sql = """
SELECT uid FROM users WHERE email = :email;
"""

# fetch user by authenticating password
# returns `uid` and `email` or none
get_user_auth_sql = """
SELECT uid, email
FROM 
    users 
WHERE
    email=:email AND
    master_pwd = crypt(:password, master_pwd);
"""

# post new user, stores email and hashed password
# returns new `uid` or none
post_user_sql = """
INSERT INTO 
    users(email, master_pwd)
VALUES 
    (:email, crypt(:password, gen_salt('bf', 8)))
RETURNING uid;
"""

# updates existing user email / password
# if password, new hash is stored
# returns `uid` or none
update_user_sql = """
UPDATE users 
SET
    email = :email,
    master_pwd = crypt(:new_password, gen_salt('bf', 8))
WHERE uid::text = :id
RETURNING uid;
"""

# deletes user by id
# cascade deletes every password associated.
# returns deleted `uid` or none
delete_user_sql = """
DELETE FROM users
WHERE 
uid::text=:id
RETURNING
    uid;
"""
