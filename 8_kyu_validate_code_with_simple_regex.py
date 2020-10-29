import re
def validate_code(code):
    return bool(re.match('[123]', str(code)))

#https://www.codewars.com/kata/56a25ba95df27b7743000016/train/python