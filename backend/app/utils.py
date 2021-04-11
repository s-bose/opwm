import string
import secrets
import random
from typing import List

__char_dump = string.ascii_letters + string.digits + string.punctuation

__DEFAULT_PWD_SIZE = 16


def gen_random_pwd(
    size: int = __DEFAULT_PWD_SIZE,
    urlsafe: bool = False
):
    if not urlsafe:
        return ''.join(secrets.choice(__char_dump) for i in range(size))
    return secrets.token_urlsafe(size)


def gen_kw_pwd(
    keywords: List[str],
    size: int = __DEFAULT_PWD_SIZE,
    include_chars: List[str] = None
):
    kw_list = set()

    if (len(''.join(keywords)) < size):
        kw_list |= set(keywords)
    else:
        while (len(''.join(list(kw_list)) + (word := secrets.choice(keywords))) < size):
            kw_list.add(word)

    # adding one more keyword exhausts the password limit
    # therefore add ligatures
    rem_space = size - len(''.join(list(kw_list)))

    # generate ligature for the remaining space
    # no alphabets, only symbols and numbers
    if include_chars is None:
        symbols = string.punctuation + string.digits
    else:
        symbols = ''.join(include_chars) + string.digits

    # generate ligature from the remainder
    ligature = ''.join(secrets.choice(symbols)
                       for i in range(rem_space))
    kw_list.add(ligature)

    passwd = ''.join(random.sample(kw_list, len(kw_list)))
    passwd = ''.join(secrets.choice([x.upper(), x]) for x in passwd)
    return passwd


def gen_pwd_from_phrase(
    phrase: str,
    size: int,
    include_chars: List[str] = None
):
    keywords = phrase.split(' ')
    return gen_kw_pwd(keywords=keywords, size=size, include_chars=include_chars)


# gen_kw_pwd(['hello', 'world'], 20, ['@', '?'])
# gen_kw_pwd(['shiladitya', 'bose', '31' 'aug', 'kolkata'],
#            20, ['@', '?', '!', '#'])
# gen_kw_pwd(['here', 'comes', 'the', 'sun'], 20, ['@'])

# gen_kw_pwd(['obama', 'come', 'eat', 'my ass', '69'], 10)

# print(gen_pwd_from_phrase('dc sucks balls', 10, ['@', '$']))
# gen_random_pwd(12)
#
