from array   import *
#1 create an array and trverse
my_array=array('i',[2,5,7,4,65,3])
for i in my_array:
    print(i)



#2  access individual element  through indexes
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tstep 2")
print(my_array[0])



#3 append the value to array using append() method
my_array.append(6)
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tstep 3")
print(my_array)



#4insert value to the array using insert method   insert(index,value)
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tstep  4")
my_array.insert(0,0)
print(my_array)


#5extend python array using extend method  extend([values])
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tstep  5")
my_array.extend([7,8])
print(my_array)



# 6 add items from list into array using fromlist() method
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tstep  6")
templist=[9,10,11]
my_array.fromlist(templist)
print(my_array)


#7 remove any array element using remove method()
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tstep  7")
my_array.remove(5)
print(my_array)



#8 remove last element using pop() method
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tstep  8")
my_array.pop()
print(my_array)


#9 Fetch any element through its index using index() method
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tstep 9")
print(my_array[5])


#10 reverse a python array using reverse method
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tstep 10")
my_array.reverse()
print(my_array)


#11 get array buffer information through buffer_info() method
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tstep 11")
print(my_array.buffer_info())



#12 check for no. of occuraces of an element using count() method
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tstep 12")
print(my_array.count(4))


#13 convert array to list using tolist() method
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tstep 13")
str = my_array.tolist()
print(str)


#14 slice array elements
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tstep 14")
print(my_array[1:10:2])
