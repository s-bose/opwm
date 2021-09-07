import string
import secrets
import random
from typing import List
from datetime import datetime, timedelta

__char_dump = string.ascii_letters + string.digits + string.punctuation

__DEFAULT_PWD_SIZE = 20


def gen_random_pwd(size_: int, urlsafe: bool = False):
    """
    Standard password generator function.
    Returns a combination of ascii characters for a given size.
    """
    if not size_:
        size_ = __DEFAULT_PWD_SIZE
    if not urlsafe:
        return "".join(secrets.choice(__char_dump) for i in range(size_))
    return secrets.token_urlsafe(size_)


def gen_kw_pwd(
    keywords: List[str], size: int = __DEFAULT_PWD_SIZE, include_chars: List[str] = None
):
    """
    A custom function that generates a password based on a list of keywords
    specified and a set of special characters specified.

    If the total size of all the keywords combined >= `size`, then we
    select a randomly chosen subset of kws out of the list such that their
    combined len < `size`

    The remaining space is filled up with numbers and special chars.
    This special block of chars is called `ligature` and together with the
    other keywords it creates a collection of text blocks, which, combined
    produce the len of `size`

    We then produce a permutation of that block list to produce a random str.
    We then randomly capitalize the letters in it.

    Parameters
    ----------

    keywords      : a list of keywords, ex: ['pizza', 'time']
    size          : size of the password
    include_chars : a list of special characters to include (default None)
                    ex: ['@', '#', '<']

    Returns
    -------

    A shiny new password
    """

    kw_list = set()

    if len("".join(keywords)) < size:
        kw_list |= set(keywords)
    else:
        while len("".join(list(kw_list)) + (word := secrets.choice(keywords))) < size:
            kw_list.add(word)

    # adding one more keyword exhausts the password limit
    # therefore add ligatures
    rem_space = size - len("".join(list(kw_list)))

    # generate ligature for the remaining space
    # no alphabets, only symbols and numbers
    if include_chars is None:
        symbols = string.punctuation + string.digits
    else:
        symbols = "".join(include_chars) + string.digits

    # generate ligature from the remainder
    ligature = "".join(secrets.choice(symbols) for i in range(rem_space))
    kw_list.add(ligature)

    passwd = "".join(random.sample(kw_list, len(kw_list)))
    passwd = "".join(secrets.choice([x.upper(), x]) for x in passwd)
    return passwd


def gen_pwd_from_phrase(phrase: str, size: int, include_chars: List[str] = None):
    keywords = phrase.split(" ")
    return gen_kw_pwd(keywords=keywords, size=size, include_chars=include_chars)


print(gen_kw_pwd(["neel", "zig", "298"], size=15))
#            20, ['@', '?', '!', '#'])
# gen_kw_pwd(['here', 'comes', 'the', 'sun'], 20, ['@'])

# gen_kw_pwd(['obama', 'come', 'eat', 'my ass', '69'], 10)

# print(gen_pwd_from_phrase('dc sucks balls', 10, ['@', '$']))
# gen_random_pwd(12)
#
