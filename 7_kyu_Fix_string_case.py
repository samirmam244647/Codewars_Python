#https://www.codewars.com/kata/5b180e9fedaa564a7000009a/train/python
import re
def solve(s):
    arr = re.findall('[A-Z]',s)
    for i in s:
        if len(arr) >  0.5 * len(s):
            return s.upper()
        else:
            return s.lower()