enable 2-step hashing\n
https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
Here there is a function called `get_password_hash` which will be used 
for registration.

#### registration
hash the plaintext master password once in the server
re-hash it in the database (pgcrypto) to store the final hash

#### login
use `OAuth2passwordForm` and `oauth2_scheme` dependency for
authenticated endpoints

#### db design
autoincremented Primary key bad idea.
need to have hash of it
