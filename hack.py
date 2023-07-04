def minimumSteps(ar1, ar2, n):
     
    # Counter to store the steps
    ans = 0
     
    # Flag to check that
    # array is converted
    flag = True
     
    # Loop until the minimum of the
    # array is greater than -1
    while min(ar1)>-1:
        a = min(ar1)
         
        # Loop to convert the array
        # elements by subtraction
        for i in range(n):
            if ar1[i]!= a:
                ar1[i]-= ar2[i]
                ans+= 1
                 
        # If the array is converted
        if len(set(ar1))== 1:
            flag = False
            print(ans)
            break
    if flag:
        print(-1)
 
# Driver Code
g = input()
ar1=input().split()
ar2=input().split()

     
    # Function Call
minimumSteps(ar1, ar2, g)