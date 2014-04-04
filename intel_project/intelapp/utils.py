import random
import string

__author__ = 'michal'


def random_string(length=6, chars=string.ascii_letters + string.digits):
        return ''.join(random.choice(chars) for _ in range(length))