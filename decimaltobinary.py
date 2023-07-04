def dtb(n):
    if(n==0 or n==1):
        return n 
    return (n%2) +10* dtb(n//2)
a=int(input("enter a decimal no to be converted into binary"))
print(dtb(a))