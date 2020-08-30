def add(num1, num2):
    return int(str(add(num1//10, num2//10)) + str(num1%10+ num2%10)) if num1*num2 else num1+num2

#https://www.codewars.com/kata/5effa412233ac3002a9e471d/train/python