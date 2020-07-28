def solve(arr):
    a = [1]
    for numbers in arr:
        a = [number * c for c in a for number in numbers]
    return max(a)

#https://www.codewars.com/kata/5d0365accfd09600130a00c9/train/python