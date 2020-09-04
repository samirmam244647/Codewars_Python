def get_a_down_arrow_of(n):
    r=[]
    for i in range(n,0,-1):
        s=''.join(str(x%10) for x in range(1,i+1))
        r.append(' '*(n-i)+s+s[::-1][1:])
    return '\n'.join(r)

#https://www.codewars.com/kata/5645b24e802c6326f7000049/train/python