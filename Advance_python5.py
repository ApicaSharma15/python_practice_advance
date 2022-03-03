#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Q1. What is the meaning of multiple inheritance?

#Inheritance is the mechanism to achieve the re-usability of code as one class(child class) can derive the properties of another class(parent class). It also provides transitivity ie. if class C inherits from P then all the sub-classes of C would also inherit from P.
#Multiple Inheritance:
#When a class is derived from more than one base class it is called multiple Inheritance. The derived class inherits all the features of the base case.
Syntax:

Class Base1:
       Body of the class

Class Base2:
     Body of the class

Class Derived(Base1, Base2):
     Body of the class


# In[ ]:


#Q2. What is the concept of delegation?

# The delegation pattern is an object-oriented design pattern that allows object composition to achieve the same code reuse as inheritance.
# Let’s say we have a Dog class that is a subclass (and thus inherits the functionality of) an Animal class. If Animal has a method called get_number_of_legs, any instantiation of the Dog class can call the get_number_of_legs method. In Python, an implementation might look like this:

class Animal:
  def __init__(self, name, num_of_legs):
    self.name = name
    self.num_of_legs = num_of_legs
  
  def get_number_of_legs(self):
    print(f"I have {self.num_of_legs} legs")

class Dog(Animal):
  def __init__(self, name, num_of_legs):
    super().__init__(name, num_of_legs)

dog = Dog('Fido', 4)
dog.get_number_of_legs()

# Outputs "I have 4 legs"
# It would be technically incorrect to say that Dog delegates get_number_of_legs to Animal because the Dog class actually has that method since it inherits the Animal class. This is what the Wikipedia definition is talking about when it refers to “code reuse.” This is what delegation will duplicate when we use composition.


# In[ ]:


#Q3. What is the concept of composition?

# Composition is a concept that models a has a relationship. It enables creating complex types by combining objects of other types. This means that a class Composite can contain an object of another class Component. This relationship means that a Composite has a Component.
# Composition is represented through a line with a diamond at the composite class pointing to the component class. The composite side can express the cardinality of the relationship. The cardinality indicates the number or valid range of Component instances the Composite class will contain.

#It is one of the fundamental concepts of Object-Oriented Programming. In this concept, we will describe a class that references to one or more objects of other classes as an Instance variable. Here, by using the class name or by creating the object we can access the members of one class inside another class. It enables creating complex types by combining objects of different classes. It means that a class Composite can contain an object of another class Component. This type of relationship is known as Has-A Relation. 
class Component:
    # composite class constructor
    def __init__(self):
        print('Component class object created...')

# composite class instance method
    def m1(self):
        print('Component class m1() method executed...')


class Composite:
    # composite class constructor
    def __init__(self):
        # creating object of component class
        self.obj1 = Component()

print('Composite class object also created...')

# composite class instance method
    def m2(self):

    print('Composite class m2() method executed...')

# calling m1() method of component class
       self.obj1.m1()


# creating object of composite class
        obj2 = Composite()

# calling m2() method of composite class
        obj2.m2()


# In[ ]:


#Q4. What are bound methods and how do we use them?

#A bound method is the one which is dependent on the instance of the class as the first argument. It passes the instance as the first argument which is used to access the variables and functions. In Python 3 and newer versions of python, all functions in the class are by default bound methods.
# Python code to demonstrate
# use of bound methods

class A:
    def func(self, arg):
        self.arg = arg
        print("Value of arg = ", arg)


# Creating an instance
obj = A()

# bound method
print(obj.func)

#Output:

< bound method A.func of <__main__.A object at 0x7fb81c5a09e8>>
Here,

 obj.func(arg) is translated by python as A.func(obj, arg).
# The instance obj is automatically passed as the first argument to the function called and hence the first parameter of the function will be used to access the variables/functions of the object.


# In[ ]:


#Q5. What is the purpose of pseudoprivate attributes?


#Python also includes the notion of name "mangling" (i.e., expansion), to localize some names in classes. This is sometimes misleadingly called private attributes really, it's just a way to localize a name to the class that created it, and does not prevent access by code outside the class. That is, this feature is mostly intended to avoid namespace collisions in instances, not to restrict access to names in general.

#Pseudo-private names are an advanced feature, entirely optional, and probably won't be very useful until you start writing large class hierarchies in multi-programmer projects. But because you may see this feature in other people's code, you need to be somewhat aware of it even if you don't use it in your own.

