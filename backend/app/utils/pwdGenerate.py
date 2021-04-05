import string
import secrets
import random
from typing import List

char_dump = string.ascii_letters + string.digits + string.punctuation


def gen_random_pwd(size: int = 20):

    passwd = ''.join(secrets.choice(char_dump) for i in range(size))
    print(passwd)


def gen_kw_pwd(
    keywords: List[str],
    size: int = 20
):
    passwd = ''
    while (len(passwd) < size):
        passwd += random.sample(keywords, 1)

    passwd = ''.join(secrets.choice(keywords) for i in range(size))
    print(passwd)


gen_kw_pwd(['hello', 'world', 'shiladitya',
           'bose', 'ghost', 'recon', '29855'], 10)
gen_kw_pwd(['hello', 'world', 'shiladitya',
           'bose', 'ghost', 'recon', '29855'], 20)
gen_kw_pwd(['hello', 'world', 'shiladitya',
           'bose', 'ghost', 'recon', '29855'], 30)
