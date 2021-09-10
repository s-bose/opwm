from typing import List
from sqlalchemy.orm import Session

from app.schemas.passwords import PasswordBase
import app.core.sql.passwords_sql as sql
from app.crud.CrudBase import CRUDBase


class CRUDPassword(CRUDBase[PasswordBase]):

    def get_pwd(
        self, 
        db: Session, 
        site: str, 
        user_id: str, 
        master_pwd: str
    ) -> PasswordBase:

        """
        Retrieves a single password entry for a `user_id`
        The stored encrypted username & password is decrypted
        using the hash of the user's `master_pwd`
    
        Parameters
        ----------
        site       : str
        user_id    : UUID
        master_pwd : str (hash)

        Returns
        -------
        id         : UUID
        site       : str
        link       : str
        username   : str
        password   : str (decrypted)
        """

        res = self.query_execute(
            db,
            query=sql.get_pwd_sql,
            params={"site": site, "user_id": user_id, "master_pwd": master_pwd},
        )

        return res

    def get_pwd_all(
        self, 
        db: Session, 
        user_id: str, 
        master_pwd: str
    ) -> List[PasswordBase]:

        """
        Retrieves all password entries for `user_id`

        Parameters
        ----------
        user_id    : UUID
        master_pwd : str (hash)

        Returns
        -------
        list
            id         : UUID
            site       : str
            link       : str
            username   : str
            password   : str (decrypted)
        """

        res = self.query_execute_all(
            db,
            query=sql.get_pwd_all_sql,
            params={"user_id": user_id, "master_pwd": master_pwd},
        )

        return res

    def post_pwd(
        self,
        db: Session,
        user_id: str,
        master_pwd: str,
        site: str,
        link: str,
        username: str,
        password: str,
    ) -> PasswordBase:

        """
        Inserts a new password entry for a `user_id`
        The password is encrypted with `PGP_SYM_ENCRYPT`
        using the stored hash of the user's master password

        Parameters
        ----------
        site       : str
        user_id    : UUID
        username   : str
        password   : str
        master_pwd : str (hash)

        Returns
        -------
        pid      : UUID

        """
        res = self.query_execute(
            db,
            query=sql.post_pwd_sql,
            params={
                "site": site,
                "link": link,
                "username": username,
                "password": password,
                "user_id": user_id,
                "master_pwd": master_pwd,
            },
        )

        return res

    def update_pwd(
        self,
        db: Session,
        user_id: str,
        master_pwd: str,
        pid: str,
        site: str,
        link: str,
        username: str,
        password: str,
    ) -> PasswordBase:

        """
        updates an entry with `pid` for a given `user_id`
        using the credentials.

        Parameters
        -----------
        user_id    : UUID
        master_pwd : str (hash)
        pid        : UUID
        site       : str
        link       : str
        username   : str
        password   : str

        Returns
        -------
        pid : UUID
        """
        res = self.query_execute(
            db,
            query=sql.update_pwd_sql,
            params={
                "user_id": user_id,
                "pid": pid,
                "master_pwd": master_pwd,
                "new_site": site,
                "new_link": link,
                "new_username": username,
                "new_password": password,
            },
        )

        return res

    def delete_pwd(
        self, 
        db: Session, 
        user_id: str, 
        pid: str
    )-> PasswordBase:
        """
        Deletes the password entry with `pid` for a
        given `user_id`
        
        Parameters
        -----------
        user_id    : UUID
        pid        : UUID

        Returns
        -------
        pid : UUID
        """
        res = self.query_execute(
            db, 
            query=sql.delete_pwd_sql, 
            params={"user_id": user_id, "pid": pid}
        )

        return res

    
    def reset_pwd_all(
        self, 
        db: Session, 
        old_master_pwd: str, 
        new_master_pwd: str, 
        user_id: str
    ):

        res = self.query_execute_all(
            db,
            query=sql.reset_pwd_all_sql,
            params={
                "old_master_pwd": old_master_pwd,
                "new_master_pwd": new_master_pwd,
                "user_id": user_id,
            },
        )

        return res


password = CRUDPassword(PasswordBase)
