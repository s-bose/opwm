from typing import List
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_password(
    site: str
) -> dict:
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
    site: str,
    username: str
):
    """
    generates a random pwd and stores it wrt the username and site
    (authenticated)
    returns the random password
    """
    return None


@router.get("/generate_kw")
def generate_kw_pwd(
    site: str,
    username: str,
    keywords: List[str]
):
    """
    generates a pwd based on the list of keywords specified
    everything else same as /generate
    (authenticated)
    """
    return None
