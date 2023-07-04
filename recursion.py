def fact(n):
    assert n>=0 and int(n)==n , "the no. must be positive integer"
    if(n==0):
        return(1)
    else:
        ans = n*fact(n-1)
        return ans
n=int(input("enter the no"))


print(fact(n))