import re

def password(s):
    return bool(re.match(r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8}', s))

#https://www.codewars.com/kata/56a921fa8c5167d8e7000053