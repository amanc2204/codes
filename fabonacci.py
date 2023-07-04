
def fabo(n):
    assert n>=0 and int(n)==n , "no must be a interger"
    if(n==0 or n==1):
        return n
    else :
        return fabo(n-1)+fabo(n-2)
n=int(input("enter no. of digits"))
for iter in range(n):
    print(fabo(iter))