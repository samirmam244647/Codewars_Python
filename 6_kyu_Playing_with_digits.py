def dig_pow(n, p):
    digits = list(str(n))
    p_add = sum = 0
    for elem in digits:
        sum += int(elem) ** (p + p_add)
        p_add += 1
        if sum % n == 0:
            return sum / n
    else:
        return -1

https://www.codewars.com/kata/5552101f47fc5178b1000050