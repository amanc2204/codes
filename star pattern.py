n=int(input('enter the value of n'))
for x in range(0,n):
    for y in range(0,n):
        if ((x+y)<n-1):
            print(" ",end='')
        else:
            print("*",end='')
    print("*"*x)