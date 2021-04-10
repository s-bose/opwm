from typing import Any, Dict
from fastapi import APIRouter

from app import utils

router = APIRouter()


@router.get("/")
def get_password(
    site: str
) -> Dict[str, Any]:
    """
    retrieves the stored pwd for site for a given user
    (authenticated)
    """
    return None


@router.post("/")
def post_password(
    site: str,
    username: str,
    passwd: str
) -> None:
    """
    stores a user-defined username/pwd for a site in vault
    (authenticated)
    """
    return None


@router.put("/")
def change_password(
    site: str,
    username: str,
    new_pwd: str
) -> None:
    """
    changes the pwd for a site
    (authenticated)
    """
    return None


@router.get("/generate")
def generate_pwd(
    size: int = None,
    urlsafe: bool = False
):
    """
    generates a random pwd and stores it wrt the username and site
    (authenticated)
    returns the random password
    """

    return {
        "password": utils.gen_random_pwd(size, urlsafe)
    }


@router.post("/generate_kw")
def generate_kw_pwd(
    size: int,
    keyword: list,
    include_char: list
):
    """
    generates a pwd based on the list of keywords specified
    everything else same as /generate
    (authenticated)
    """

    return {
        "password": utils.gen_kw_pwd(keyword, size, include_char)
    }
