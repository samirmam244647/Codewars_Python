import re
def check_password(s):
    if re.search('^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?\d)(?=.*?[!@#$%^&*?])[a-zA-Z\d!@#$%^&*?]{8,20}$', s) :
        return 'valid'
    else:
        return 'not valid'

#https://www.codewars.com/kata/57e35f1bc763b8ccce000038