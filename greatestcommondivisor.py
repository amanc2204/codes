#this can be done by eculidean algorthm
def gcd(a,b):
    assert a==int(a) and b==int(b) , "the no must be  an integer"
    if(a<0):
        a=-1*a
    if(b<0):
        b=-1*b
    if (b==0):
        return a
    else:
        return gcd(b,a%b)
c=int(input("enter the first no,"))
d=int(input("enter the second no."))
if(c>d):
    print("the highest common facor is ",gcd(c,d))
else:
     print("the highest common facor is ",gcd(d,c))