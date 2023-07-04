def sod(n):
    if(n==0):
        return 0
    else :
        return n%10+sod(int(n/10))
print(sod(00000))
