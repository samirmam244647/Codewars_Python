import re
def getCount(inputStr):
    num_vowels = re.compile(r'[a,e,i,o,u]')
    a = num_vowels.findall(inputStr)
    return len(a)

#https://www.codewars.com/kata/54ff3102c1bad923760001f3