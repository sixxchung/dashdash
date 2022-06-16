# sub/bbb.py
from .aaa import multiply

# from sub.aaa import multiply
# from aaa import multiply


def bbb(a, b):
    return multiply(a, b) + (a+b)
