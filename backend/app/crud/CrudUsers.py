from sqlalchemy.orm import Session
from pydantic import EmailStr

from app.schemas.user import UserBase

import app.core.sql.users_sql as sql
from app.crud.CrudBase import CRUDBase

class CRUDUsers(CRUDBase[UserBase]):


    def get_user_by_id(self, db: Session, id: str) -> UserBase:
        """
        ### used internally via API dependencies

        Fetches user information from the `User` table by
        querying by their id (uuid primary key)

        Parameters
        ----------
        id : UUID

        Returns
        -------
        uid         : UUID
        email       : EmailStr
        master_pwd  : str (hash)

        """
        return self.query_execute(
            db,
            query=sql.get_user_by_id_sql,
            params={
                "id": id
            }
        )
   

    def get_user_by_email(self, db: Session, email: EmailStr) -> UserBase:

        """
        ### Only used internally via API dependencies

        Fetches user information from the `User` table by querying
        by their registered email address.

        Parameters
        ----------
        email : EmailStr
        
        Returns
        -------
        uid : UUID

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

        postgres `crypt()` is used to verify the supplied password 
        with the stored hash.
        
        Parameters
        ----------
        email    : EmailStr
        password : str 

        Returns
        -------
        uid    : UUID
        email  : EmailStr

        """
        return self.query_execute(
            db,
            query=sql.get_user_auth_sql,
            params={
                "email": email,
                "password": password
            }
        )
  


    def post_user(
        self, 
        db: Session, 
        email: str, 
        password: str
    ) -> UserBase:

        """
        Inserts a newly registered user's email and their hashed
        master password in the `Users` table.

        Uses `crypt()` function with salt to generate and store 
        hashes of passwords.
        `Blowfish (bf)` hashing with 8 iterations is used.

        Parameters
        ----------
        email    : EmailStr
        password : str

        Returns
        -------
        uid : UUID
        """

        return self.query_execute(
            db,
            query=sql.post_user_sql,
            params={
                "email": email,
                "password": password
            }
        )


    def update_user(
        self, 
        db: Session, 
        _id: str, 
        email: str, 
        new_password: str
    ) -> UserBase:

        """
        Updates an existing user by changing
        the old master password hash with a new one.
        
        This does not update the existing username/passwords
        stored in the `Passwords` table
        For that, an additional query on `Passwords` table
        needs to be applied.

        Parameters
        ----------
        email        : EmailStr
        new_password : str

        Returns
        -------
        uid : UUID

        """
        return self.query_execute(
            db,
            query=sql.update_user_sql,
            params={
                "email": email,
                "new_password": new_password,
                "id": _id
            }
        )
    

    def delete_user(self, db: Session, _id: str)-> UserBase:

        """
        Deletes an existing user by `_id`
        Cascade deletes all passwords associated with it.

        Parameters
        ----------
        _id: UUID

        Returns
        -------
        uid: UUID (deleted entry)
        """
        return self.query_execute(
            db, query=sql.delete_user_sql, params={
                "id": _id,
            }
        )

user = CRUDUsers(UserBase)