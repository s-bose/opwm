from app.models.user import User
from sqlalchemy.orm import Session
from pydantic import EmailStr

from app.schemas.user import UserBase

import app.core.sql.users_sql as sql
from app.crud.CrudBase import CRUDBase

class CRUDUsers(CRUDBase[UserBase]):


    def get_user_by_id(self, db: Session, id: str) -> UserBase:
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
        return self.query_execute(
            db,
            query=sql.get_user_by_id_sql,
            params={
                "id": id
            }
        )
   

    def get_user_by_email(self, db: Session, email: EmailStr) -> str:

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
        return self.query_execute(
            db,
            query=sql.get_user_by_email_sql,
            params={
                "email": email
            }
        )
        


    def get_user(self, db: Session, email: str, password: str) -> UserBase:

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
        return self.query_execute(
            db,
            query=sql.get_user_auth_sql,
            params={
                "email": email,
                "password": password
            }
        )
  


    def post_user(self, db: Session, email: str, password: str) -> str:

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
        return self.query_execute(
            db,
            query=sql.post_user_sql,
            params={
                "email": email,
                "password": password
            }
        )


    def update_user(self, db: Session, id: str, email: str, new_password: str) -> UserBase:

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
        return self.query_execute(
            db,
            query=sql.update_user_sql,
            params={
                "email": email,
                "new_password": new_password,
                "id": id
            }
        )

user = CRUDUsers(UserBase)