def solution(digits):
    result = [int(digits[i:i+5]) for i in range(0,len(digits)-4)]
    return max(result)

#https://www.codewars.com/kata/51675d17e0c1bed195000001