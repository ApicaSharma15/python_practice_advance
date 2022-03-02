#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Q1. What is the relationship between classes and modules?

# When you save a class into a separate file, that file is called a module. You can have any number of classes in a single module. There are a number of ways you can then import the class you are interested in.

example:
    A module is simply a file that contains one or more classes or functions:
        
# Save as rocket.py
from math import sqrt

class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self, x=0, y=0):
        # Each rocket has an (x,y) position.
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        # Move the rocket according to the paremeters given.
        #  Default behavior is to move the rocket up one unit.
        self.x += x_increment
        self.y += y_increment
        
    def get_distance(self, other_rocket):
        # Calculates the distance from this rocket to another rocket,
        #  and returns that value.
        distance = sqrt((self.x-other_rocket.x)**2+(self.y-other_rocket.y)**2)
        return distance
    

class Shuttle(Rocket):
    # Shuttle simulates a space shuttle, which is really
    #  just a reusable rocket.
    
    def __init__(self, x=0, y=0, flights_completed=0):
        super().__init__(x, y)
        self.flights_completed = flights_completed
        
Now you can import the Rocket and the Shuttle class, and use them both in a clean uncluttered program file:
    
# Save as rocket_game.py
from rocket import Rocket, Shuttle

rocket = Rocket()
print("The rocket is at (%d, %d)." % (rocket.x, rocket.y))

shuttle = Shuttle()
print("\nThe shuttle is at (%d, %d)." % (shuttle.x, shuttle.y))
print("The shuttle has completed %d flights." % shuttle.flights_completed)


# In[ ]:


#Q2. How do you make instances and classes?

#To create instances of a class, you call the class using class name and pass in whatever arguments its __init__ method accepts.
#Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by its class) for modifying its state.
#When a class defines an __init__() method, class instantiation automatically invokes __init__() for the newly-created class instance.
# Of course, the __init__() method may have arguments for greater flexibility. In that case, arguments given to the class instantiation operator are passed on to __init__(). For example,

 class Complex:
        def __init__(self, realpart, imagpart):
            self.r = realpart
            self.i = imagpart

x = Complex(3.0, -4.5)
x.r, x.i
(3.0, -4.5)


# In[ ]:


#Q3. Where and how should be class attributes created?

# Class attributes belong to the class itself they will be shared by all the instances. Such attributes are defined in the class body parts usually at the top, for legibility.

# Accessed using class name as well as using object with dot notation, e.g. classname.class_attribute or object.class_attribute

# Changing value by using classname.class_attribute = value will be reflected to all the objects.

# The following example demonstrates the use of class attribute count.:
class Student:
    count = 0
    def __init__(self):
        Student.count += 1                
        
#In the above example, count is an attribute in the Student class. Whenever a new object is created, the value of count is incremented by 1. You can now access the count attribute after creating the objects, as shown below.
std1=Student()
Student.count

std2 = Student()
Student.count


# In[ ]:


#Q4. Where and how are instance attributes created?


#An instance attribute is a Python variable belonging to one, and only one, object. This variable is only accessible in the scope of this object and it is defined inside the constructor function, __init__(self,..) of the class.
# The following demonstrates the instance attributes: 
class Student:
    def __init__(self, name, age): 
        self.name = name
        self.age = age
        
# Now, you can specify the values while creating an instance, as shown below.
std = Student('Bill',25)
std.name
'Bill'
std.age
25
std.name = 'Steve'
std.age = 45
std.name
'Steve'
std.age
45
        





# In[ ]:


#Q5. What does the term "self" in a Python class mean?

# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# self represents the instance of the class. By using the “self” keyword we can access the attributes and methods of the class in python. It binds the attributes with the given arguments.
# The reason you need to use self. is because Python does not use the @ syntax to refer to instance attributes. Python decided to do methods in a way that makes the instance to which the method belongs be passed automatically, but not received automatically: the first parameter of methods is the instance the method is called on.
# Write Python3 code here

class car():
    # init method or constructor
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def show(self):
        print("Model is", self.model )
        print("color is", self.color )

# both objects have different self which
# contain their attributes
audi = car("audi a4", "blue")
ferrari = car("ferrari 488", "green")

audi.show()	 # same output as car.show(audi)
ferrari.show() # same output as car.show(ferrari)




# In[ ]:


#Q6. How does a Python class handle operator overloading?

# Operator Overloading means giving extended meaning beyond their predefined operational meaning. For example operator + is used to add two integers as well as join two strings and merge two lists. It is achievable because ‘+’ operator is overloaded by int class and str class. You might have noticed that the same built-in operator or function shows different behavior for objects of different classes, this is called Operator Overloading. 
# Consider that we have two objects which are a physical representation of a class (user-defined data type) and we have to add two objects with binary ‘+’ operator it throws an error, because compiler don’t know how to add two objects. So we define a method for an operator and that process is called operator overloading. We can overload all existing operators but we can’t create a new operator. To perform operator overloading, Python provides some special function or magic function that is automatically invoked when it is associated with that particular operator. For example, when we use + operator, the magic method __add__ is automatically invoked in which the operation for + operator is defined.
# example # Python Program to perform addition of two complex numbers using binary + operator overloading: 

class complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

# adding two objects
def __add__(self, other):
    return self.a + other.a, self.b + other.b

Ob1 = complex(1, 2)
Ob2 = complex(2, 3)
Ob3 = Ob1 + Ob2
print(Ob3)


# In[ ]:


#Q7. When do you consider allowing operator overloading of your classes?

#Python operators work for built-in classes. But the same operator behaves differently with different types. For example, the + operator will perform arithmetic addition on two numbers, merge two lists, or concatenate two strings.

# This feature in Python that allows the same operator to have different meaning according to the context is called operator overloading.

# So what happens when we use them with objects of a user-defined class? Let us consider the following class, which tries to simulate a point in 2-D coordinate system.
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


p1 = Point(1, 2)
p2 = Point(2, 3)
print(p1+p2)

#output
Traceback (most recent call last):
  File "<string>", line 9, in <module>
    print(p1+p2)
TypeError: unsupported operand type(s) for +: 'Point' and 'Point'
        
# Here, we can see that a TypeError was raised, since Python didn't know how to add two Point objects together.

# However, we can achieve this task in Python through operator overloading. Using special functions, we can make our class compatible with built-in functions.
#Suppose we want the print() function to print the coordinates of the Point object instead of what we got. We can define a __str__() method in our class that controls how the object gets printed. Let's look at how we can achieve this:

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    
#Now let's try the print() function again.
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)


p1 = Point(2, 3)
print(p1)

#output
(2, 3)
#So, when you use str(p1) or format(p1), Python internally calls the p1.__str__() method. Hence the name, special functions.

#To overload the + operator, we will need to implement __add__() function in the class. With great power comes great responsibility. We can do whatever we like, inside this function. But it is more sensible to return a Point object of the coordinate sum.

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)


p1 = Point(1, 2)
p2 = Point(2, 3)

print(p1+p2)

#output
(3,5)


# In[ ]:


#Q8. What is the most popular form of operator overloading?

#A very popular and convenient example is the Addition (+) operator. Just think how the '+' operator operates on two numbers and the same operator operates on two strings. It performs “Addition” on numbers whereas it performs “Concatenation” on strings.


# In[ ]:


#Q9. What are the two most important concepts to grasp in order to comprehend Python OOP code?

# inheritance and polymorphism

#Inheritance is the procedure in which one class inherits the attributes and methods of another class.  The class whose properties and methods are inherited is known as Parent class. And the class that inherits the properties from the parent class is the Child class.The interesting thing is, along with the inherited properties and methods, a child class can have its own properties and methods.How to inherit a parent class? Use the following syntax:
class Car:          #parent class

    def __init__(self, name, mileage):
        self.name = name 
        self.mileage = mileage 

    def description(self):                
        return f"The {self.name} car gives the mileage of {self.mileage}km/l"

class BMW(Car):     #child class
    pass

class Audi(Car):     #child class
    def audi_desc(self):
        return "This is the description method of class Audi."
obj1 = BMW("BMW 7-series",39.53)
print(obj1.description())

obj2 = Audi("Audi A8 L",14)
print(obj2.description())
print(obj2.audi_desc())

#We have created two child classes namely “BMW” and “Audi” who have inherited the methods and properties of the parent class “Car”.  We have provided no additional features and methods in the class BMW. Whereas one additional method inside the class Audi.

#Notice how the instance method description() of the parent class is accessible by the objects of child classes with the help of obj1.description() and obj2.description(). And also the separate method of class Audi is also accessible using obj2.audi_desc().

#Polymorphism
#This is a Greek word. If we break the term Polymorphism, we get “poly”-many and “morph”-forms. So Polymorphism means having many forms. In OOP it refers to the functions having the same names but carrying different functionalities.

class Audi:
  def description(self):
    print("This the description function of class AUDI.")

class BMW:
  def description(self):
    print("This the description function of class BMW.")
audi = Audi()
bmw = BMW()
for car in (audi,bmw):
 car.description()

#When the function is called using the object audi then the function of class Audi is called and when it is called using the object bmw then the function of class BMW is called.

