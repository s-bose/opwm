import string
import secrets
import random
import tokenize
from typing import List

char_dump = string.ascii_letters + string.digits + string.punctuation


def gen_random_pwd(size: int = 20):

    passwd = ''.join(secrets.choice(char_dump) for i in range(size))
    print(passwd)


def gen_kw_pwd(
    keywords: List[str],
    size: int = 20,
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

    # print(kw_list)
    kw_list = list(kw_list)
    # print(kw_list)
    # random.shuffle(kw_list)
    passwd = ''.join(random.sample(kw_list, len(kw_list)))
    print(passwd)


def gen_pwd_from_phrase(
    phrase: str,
    size: int,
    include_chars: List[str] = None
):
    keywords = phrase.split(' ')
    gen_kw_pwd(keywords=keywords, size=size, include_chars=include_chars)


# gen_kw_pwd(['hello', 'world'], 20, ['@', '?'])
# gen_kw_pwd(['shiladitya', 'bose', '31' 'aug', 'kolkata'],
#            20, ['@', '?', '!', '#'])
# gen_kw_pwd(['here', 'comes', 'the', 'sun'], 20, ['@'])

# gen_kw_pwd(['obama', 'come', 'eat', 'my ass', '69'], 10)

gen_pwd_from_phrase('I eat ass everyday', 20)
# gen_random_pwd(12)
#
