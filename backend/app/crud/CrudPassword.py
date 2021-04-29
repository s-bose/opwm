from sqlalchemy.orm import Session

from app.schemas.passwords import PasswordBase
import app.core.sql.passwords_sql as sql
from app.crud.CrudBase import CRUDBase

class CRUDPassword(CRUDBase[PasswordBase]):

    def get_pwd(self, db: Session, site: str, user_id: str, master_pwd: str) -> PasswordBase:
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

        PasswordBase model

        id         : uuid primary key of the password record, as str
        site       : name of the site
        username   : decrypted plaintext username
        password   : decrypted plaintext username
        """

        res = self.query_execute(
            db,
            query=sql.get_pwd_sql,
            params={
                "site": site, 
                "user_id": user_id, 
                "master_pwd": master_pwd
            },
        )

        return res

    def get_pwd_all(self, db: Session, user_id: str, master_pwd: str) -> PasswordBase:
        """
        Retrieves all the stored credentials for the logged in user.

        Parameters
        ----------

        user_id    : uuid of the logged in user
        master_pwd : stored hash of the user's master password

        Returns
        -------

        list
            a list of PasswordBase models

            id         : uuid primary key, as str
            site       : name of the site
            username   : decrypted plaintext username
            password   : decrypted plaintext username
        """

        res = self.query_execute_all(
            db,
            query=sql.get_pwd_all_sql,
            params={
                "user_id": user_id,
                "master_pwd": master_pwd
            }
        )

        return res

    def post_pwd(
        self, db: Session, site: str, user_id: str, username: str, password: str, master_pwd: str
    ) -> PasswordBase:
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

        id   : uuid primary key of inserted row, as str

        """
        res = self.query_execute(
            db,
            query=sql.post_pwd_sql,
            params={
                "site": site,
                "user_id": user_id,
                "username": username,
                "password": password,
                "master_pwd": master_pwd,
            }
        )

        return res
        


    def update_pwd(
        self,
        db: Session,
        site: str,
        user_id: str,
        new_username: str,
        new_password: str,
        master_pwd: str,
    ) -> PasswordBase:

        """
        updates a single username/password entry for a given `site`

        """
        res = self.query_execute(
            db,
            query=sql.update_pwd_sql,
            params={
                "site": site,
                "user_id": user_id,
                "username": new_username,
                "password": new_password,
                "master_pwd": master_pwd,
            }
        )
        
        return res



    def reset_pwd_all(self, db: Session, old_master_pwd: str, new_master_pwd: str, user_id: str):
        
        res = self.query_execute_all(
            db,
            query=sql.reset_pwd_all_sql,
            params={
                "old_master_pwd": old_master_pwd,
                "new_master_pwd": new_master_pwd,
                "user_id": user_id,
            }
        )
        
        return res
        

password = CRUDPassword(PasswordBase)