# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 21:53:05 2024

@author: Manish Ranjit
"""


################# Lesson 1 Class and Objects #######################
#Class is a blueprint through which onjects (instances) are made.

class computer:
    def config(self):
        print("This is i5, 16gb, 1TB computer")
        
        
        
com1 = computer()

print(type(com1))

computer.config(com1) #human walk manish

com1.config()#manish walk #com1 is passed as self

################# Lesson 2 __init__ method in Python #######################

class computer:
    def __init__(self):
        print("in init")
    
    def config(self):
        print("This is i5, 16gb, 1TB computer")
        
com1 = computer() #Prints "in init"

#------------------------
class computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
    
    def config(self):
        print(f"Configuration of is {self.cpu} and {self.ram} gb ram")
        
com1 = computer('i5',16)
com1.config()

################# Lesson 3 Constructor, Self and Comparing Objects ##########

class computer:
    pass

c1 = computer()
c2 = computer()

print(id(c1))
print(id(c2))
'''Everytime an object is created it is allocated to new space'''
'''Size of object? -> Depends on number of variables'''
'''Who allocates size to object? -> constructor'''
''' () in computer() is a contrcutor and it calls initi method'''

#------------------------
class computer:
    def __init__(self):
        self.name = "Manish"
        self.age = 39

c1 = computer()
c2 = computer()

c1.name = "apple"
c1.age = 15

c2.name = "cat"
c2.age = 25

print(c1.name, c1.age)
print(c2.name, c2.age)

#------------------------
class computer:
    def __init__(self):
        self.name = "Manish"
        self.age = 39
        
    def update(self): #self is apointer directing towards c1 or c2
        self.age = 30

c1 = computer()
c2 = computer()

c1.name = "apple"
c1.age = 15
c1.update()

c2.name = "cat"
c2.age = 25
c2.update()

print(c1.name, c1.age)
print(c2.name, c2.age)


#------------------------
class computer:
    def __init__(self):
        self.name = "Manish"
        self.age = 39

    def compare(self,other): 
        if self.age == other.age:
            return True
        else: 
            return False      
 

c1 = computer()
c2 = computer()

c1.name = "apple"
c1.age = 15

c2.name = "cat"
c2.age = 25

if c1.compare(c2):
    print("They are of same age")
else:
    print("They are of different age")    

################# Lesson 4 Types of variables in Python ##########
''' Instance variable and Class (Static) Variable'''

class car:
    
    wheels = 4 #Class variable. It is fixed for all the objects
    
    def __init__(self): #Instance variable are different for diff objects
        self.milage = 10
        self.company = "BMW"
        
c1 = car()
c2 = car()

print(c1.company,c1.milage, c1.wheels)
print(c1.company,c1.milage, car.wheels)

#------------------------
'''namespace: area where we create and store object/variable'''
'''Class namespace: where all class variables are stored -> Wheels'''
'''instance namespace: where all instance variables are stored ->milage, company'''
class car:
    
    wheels = 4 #Class variable. It is fixed for all the objects
    
    def __init__(self): #Instance variable are different for diff objects
        self.milage = 10
        self.company = "BMW"
        
c1 = car()
c2 = car()

c2.company = "Tesla"
c2.milage = 25

car.wheels = 5

print(c1.company,c1.milage, c1.wheels)
print(c2.company,c2.milage, car.wheels)

################# Lesson 5 Types of Methods in Python ##########
'''Instance Methods, class methods and static methods'''

class student:
    
    school = "Telusko"
    
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):#instance method as we pass self
        return (self.m1 +self.m2 + self.m3)/3


s1 = student(32,55,73)
s2 = student(53,89,93)
print(s1.avg())
print(s2.avg())

#------------------------
'''Accessor Method: Only Fetching value of instance variable
  Mutator Method: Modifying value of instance variable '''  

class student:
    
    school = "Telusko"
    
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):#instance method as we pass self
        return (self.m1 +self.m2 + self.m3)/3
    
    def get_m1(self): #Accessor Method
        return self.m1
    
    def set_m1(self, f): #Mutator Method
        self.m1 = f

s1 = student(32,55,73)
s2 = student(53,89,93)
print(s1.avg())
print(s2.avg())

#------------------------
'''class method'''

class student:
    
    school = "Telusko"
    
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):#instance method as we pass self
        return (self.m1 +self.m2 + self.m3)/3
   
    @classmethod #This is decorator
    def info(cls):#change school name for all objects. cls: class
        return cls.school

s1 = student(32,55,73)
s2 = student(53,89,93)

print(s1.avg())
print(student.info())


#------------------------
'''Static method'''

class student:
    
    school = "Telusko"
    
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):#instance method as we pass self
        return (self.m1 +self.m2 + self.m3)/3
   
    @classmethod #This is decorator
    def getSchool(cls):#change school name for all objects. cls: class
        return cls.school
    
    @staticmethod #decorator
    def info(): #Neither related to object (no self) or class (no cls)
        print("This is Student class in abc module")

s1 = student(32,55,73)
s2 = student(53,89,93)

print(s1.avg())

student.info()


################# Lesson 6 Inner classes in Python ##########

class student:
    def __init__(self,name,num,laptopName, processor, ram):
        self.name = name
        self.num = num
        self.laptopName = laptopName
        self.processor = processor
        self.ram = ram
    def show(self):
        print(self.name, self.num, self.laptopName)        
    
s1 = student('Manish',5, "HP", "I5",8)
s2 = student('Apple',7, "HP", "I5",8)

s1.show()

#------------------------
class student:#Outer class
    def __init__(self,name,num):
        self.name = name
        self.num = num
        self.lap = self.laptop() #inner class called
     
    def show(self):
        print(self.name, self.num)    
        
    class laptop:  #inner class
        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = 8
    
s1 = student('Manish',5)
s2 = student('Apple',7)

s1.show()
print(s1.lap.brand)

lap1 = s1.lap
lap2 = s2.lap

print(id(lap1))
print(id(lap2))

lap1 = student.laptop()
#------------------------
'''You can create object of inner class inside the outer class
or
you can create object of inner class outside the outer class
provided tyou use outer class name to call it'''

class student:#Outer class
    def __init__(self,name,num):
        self.name = name
        self.num = num
        self.lap = self.laptop() #inner class called
     
    def show(self):
        print(self.name, self.num)    
        self.lap.show() #inlcuded this
        
    class laptop:  #inner class
        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = 8
        def show(self):
            print(self.brand, self.cpu,self.ram) 
            
            
s1 = student('Apple',5)
s2 = student('Cat',7)

s1.show()


################# Lesson 7 Inheritance in Python ##########












