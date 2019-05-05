# *_*coding:utf-8 *_*
from functools import reduce

def normalize(name):
    a = name[0].upper()
    b = name[1:].lower()
    return a + b


def prod(L):
    return reduce(lambda x, y : x * y, L)

