# Dict = {1: 'Geeks', 2: 'For',
#         3:{'A' : 'Welcome', 'B' : 'To', 'C' : 'Geeks'}}
#
# print(Dict.items())
# i = 0
# while (i < 3):
#         i = i + 1
#         print("Hello Geek")
#
# # checks if list still
# # contains any element
# a = [1, 2, 3, 4]
# while a:
#         print(a.pop())
#
# i = 10
# while i < 12:
#         i += 1
#         print(i)
# else: # Not executed as there is a break
#         print("No Break")
# def myFun(**kwargs):
#         print(kwargs.items())
#
#
#
# # Driver code
# myFun(first='Geeks', mid='for', last='Geeks')
# Python program to demonstrate
# encapsulation

# Creating a Base class
# class Base:
#         def __init__(self):
#                 self.a = "GeeksforGeeks"
#                 self._c = "GeeksforGeeks"
#
# # Creating a derived class
# class Derived(Base):
#         def __init__(self):
#
#                 # Calling constructor of
#                 # Base class
#                 Base.__init__(self)
#                 print("Calling private member of base class: ")
#                 print(self.__c)
#                 # Driver code
# obj = Derived()
# Program to depict else clause with try-except
# Python 3
# Function which returns a/b
def AbyB(a , b):
        try:
                c = ((a+b) / (a-b))
        except :
                print ("a/b result in 0")
        else:
                print (c)

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
