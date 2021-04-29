get_user_by_id_sql = """
SELECT * FROM users WHERE uid::text = :id;
"""

get_user_by_email_sql = """
SELECT uid FROM users WHERE email=:email;
"""

get_user_auth_sql = """
SELECT uid, email
FROM 
    users 
WHERE
    email=:email AND
    master_pwd = crypt(:password, master_pwd);
"""

post_user_sql = """
INSERT INTO 
    users(email, master_pwd)
VALUES 
    (:email, crypt(:password, gen_salt('bf', 8)))
RETURNING uid;
"""

update_user_sql = """
UPDATE users 
SET
    email = :email,
    master_pwd = crypt(:new_password, gen_salt('bf', 8))
WHERE uid::text = :id
RETURNING uid, email;
"""