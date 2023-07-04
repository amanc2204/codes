'''
class Dog:
    species="mammal"              #static member
    def __init__(self,breed,name):
        self.breed=breed
        self.name=name
    def bark(self):
        print("woof!")

my_dog=Dog('lab','tommy')
print(type(my_dog))
print(my_dog.breed)
my_dog.bark()
'''



'''
class Circle:
    pi=3.14
    def __init__(self,radius=1):
        self.radius=radius
        self.area=radius*radius* self.pi   #we can use Circle.pi in place of self.pi
    def circumference(self):
        return self.radius*self.pi*2
my_circle=Circle(4)
my_circle2=Circle(5)
print(my_circle.pi)
print(my_circle.area)
print(my_circle2.area)
print(my_circle.radius)
print(my_circle.circumference())

'''



#inheritence
'''

class Animal():
    name='dog'
    def __init__(self):
        print("animal created")
    def who_am_i(self):
        print("i am an animal")
    def eat(self):
        print("i am eating ")
my_Animal=Animal()
print(Animal.name)
print(type(my_Animal))
print(len(my_Animal))
my_Animal.name='GG'
print(my_Animal.name)
print(Animal.name)
my_Animal.who_am_i()
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("dog created")
    def bark(self):
        print("i am barking")
my_dog=Dog()
my_dog.who_am_i()   #we dont created who_am_i in dog class but still we can call this method by the instance of dog because we inherited animal in dog class
my_dog.bark()
#multilevel inheritence
class labra(Dog):
    def __init__(self):
        Dog.__init__(self)
        print("labra crated")
    def eat(self):
        Dog.bark(self)

my_labra=labra()
my_labra.eat()
print(my_labra)
'''


#MAGIC METHODS

class Book():
    def __init__(self,tittle,author,pages):
        self.tittle=tittle
        self.author=author
        self.pages=pages
    def __str__(self):
        return self.tittle +" by "+ self.author
    def __len__(self):
        return 500
    def __del__(self):
        print(" the object has been deleted ")


b=Book('python','aman','500')
print(b)
print(len(b))

#delete function in python class
del b




'''
#CHALLENGE from course
class Account():
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def __str__(self):
        return "Account owner : "+ self.owner +"\nAccount balance: $"+str(self.balance)
    def deposite(self,dep):
        self.balance=self.balance+dep
        print("deposit accepted")
    def withdraw(self,deb):
        if self.balance>=deb:
            self.balance=self.balance-deb
            print("withdrawl accepted")
        else:
            print("insufficient balance")
            print("remaining funds = ",self.balance)



acct1=Account('josh',100)
print(acct1)
acct1.deposite(500)
print(acct1)
acct1.withdraw(600)
print(acct1)
acct1.withdraw(600)
'''

