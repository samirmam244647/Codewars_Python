import random
def scrolling_text(string):
    string = string.upper()
    texts = []
    for char in string:
        texts.append(string)
        string = string[1:] + string[0]
    return texts

#https://www.codewars.com/kata/5a995c2aba1bb57f660001fd