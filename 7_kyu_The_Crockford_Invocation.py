#https://www.codewars.com/kata/57e7d21f6603f6e31f00007c/train/python

def add(a):
    return lambda x: x + a


def subtract(a):
    return lambda x: a - x


def multiply(a):
    return lambda x: x * a


def apply(a):
    return lambda x: a(x)