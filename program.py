def pow(n,a):
    if a<=0:
        return 1
    else:
        return n * pow(n,a-1)
def fact(n):
    if n<=1:
         return 1
    else:
        return n* fact(n-1)
def abc(n):
    assert n>=0 and int(n)==n , "wrong input"
    if n<=0:
        return 0
    else:
        return ((n * pow(n,n)) / fact(n)) + abc(n-1)

m=abc(3)
print(m)