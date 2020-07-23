def solve(s):
    arr = [0, 0, 0, 0]
    for i in s:
        if i.isupper():
            arr[0] +=1
        elif i.islower():
            arr[1] +=1
        elif i.isdigit():
            arr[2] +=1
        else:
            arr[3] +=1
    return arr

#https://www.codewars.com/kata/5a29a0898f27f2d9c9000058/train/python