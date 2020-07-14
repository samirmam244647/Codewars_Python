def halving_sum(n):
    a = n
    while n//2>=1:
        n //=2
        a += n
    return a

#Given a positive integer n, calculate the following sum:
#n + n/2 + n/4 + n/8 + ...
#All elements of the sum are the results of integer division
#Example
#25  =>  25 + 12 + 6 + 3 + 1 = 47