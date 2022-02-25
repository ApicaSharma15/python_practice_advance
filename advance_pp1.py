#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input("Q1. What is the purpose of Python's OOP");get_ipython().run_line_magic('pinfo', 'OOP')


## In Python, object-oriented Programming (OOPs) is a programming paradigm that uses objects and classes in programming. It aims to implement real-world entities like inheritance, polymorphisms, encapsulation, etc.


# In[ ]:


get_ipython().set_next_input('Q2. Where does an inheritance search look for an attribute');get_ipython().run_line_magic('pinfo', 'attribute')


#Inheritance is when a class is created based on an existing class, and the new class inherits the attributes and methods from the existing class. The new class is usually called “child class”, and the existing class is called “parent class”.
#In Python, inheritance happens when an object is qualified, and involves searching an attribute definition tree (one or more namespaces). Every time you use an expression of the form object.attr where object is an instance or class object, Python searches the namespace tree at and above object, for the first attr it can find. Because lower definitions in the tree override higher ones, inheritance forms the basis of specialization.


# In[ ]:


get_ipython().set_next_input('Q3. How do you distinguish between a class object and an instance object');get_ipython().run_line_magic('pinfo', 'object')

#class object:
when we create a class in python then a class object is created so whenever python finds a class statement in the whole program then it creates a class object and assigns a name to that object i.e. class name. As we know in python, everything is an object so the class itself is an object and is the instance of metaclasses. Look at the following example

class MyClass:
 pass
above code will generate a class object and name it ‘MyClass’. From this class object, we will create instance objects.
#Class objects provide default behavior and serve as factories for instance objects
#The class object comes from the ‘class’ statement in code. whenever we encounter a class statement then a class object will be created.
#class object inherits the attributes of its parent classes.

#Instance object:
when we call a class, it creates an instance object of that class from which the object has been created. For example when we call the above-created class then it will create an instance object like this.


Obj1=MyClass()
The above statement creates an object and names it to Obj1 which is an instance of MyClass.

#Instance objects are real objects in your python code process. The instance object has access to attributes of the class from which it is created. For example, Obj1 is the instance of class MyClass so, Now Obj1 can access everything defined in the class, and in the class object, we define the default behavior and properties of objects.
#The instance object comes from a call i.e. when we call the class. Actually, we are creating instance objects of that class.
.
#Instance object inherits the attributes of the class object from which it was created

#class object is like a blueprint for intance object but instance object is a concrete item in out code.
#instance objects are new namespaces, thay start out empty but inherit object attributes that live in class object.
#The first argumetn of class functions(self) reference the instance object and assignments to attributes of self change data in the instance.


# In[ ]:


get_ipython().set_next_input('Q4. What makes the first argument in a class’s method function special');get_ipython().run_line_magic('pinfo', 'special')

# The first argument of every class method, including init, is always a reference to the current instance of the class. By convention, this argument is always named self. In the init method, self refers to the newly created object; in other class methods, it refers to the instance whose method was called.

#Self is the first argument to be passed in Constructor and Instance Method. Self must be provided as a First parameter to the Instance method and constructor. If you don't provide it, it will cause an error.


# In[ ]:


get_ipython().set_next_input('Q5. What is the purpose of the __init__ method');get_ipython().run_line_magic('pinfo', 'method')

The __init__ function is called every time an object is created from a class. The __init__ method lets the class initialize the object's attributes and serves no other purpose. It is only used within classes.

"__init__" is a reseved method in python classes. It is known as a constructor in object oriented concepts. This method called when an object is created from the class and it allow the class to initialize the attributes of a class.

Create a class named Person, use the __init__() function to assign values for name and age:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


# In[ ]:


get_ipython().set_next_input('Q6. What is the process for creating a class instance');get_ipython().run_line_magic('pinfo', 'instance')

get_ipython().set_next_input('What is the process for creating a class instance in Python');get_ipython().run_line_magic('pinfo', 'Python')
Use the class name to create a new instance

Call ClassName() to create a new instance of the class ClassName . To pass parameters to the class instance, the class must have an __init__() method. Pass the parameters in the constructor of the class.


# In[ ]:


get_ipython().set_next_input('Q7. What is the process for creating a class');get_ipython().run_line_magic('pinfo', 'class')

To create a class, use the keyword class:
Create a class named MyClass, with a property named x:

class MyClass:
  x = 5


# In[ ]:


get_ipython().set_next_input('Q8. How would you define the superclasses of a class');get_ipython().run_line_magic('pinfo', 'class')

The class from which a class inherits is called the parent or superclass. A class which inherits from a superclass is called a subclass, also called heir class or child class. Superclasses are sometimes called ancestors as well.

A superclass is the class from which many subclasses can be created. The subclasses inherit the characteristics of a superclass. The superclass is also known as the parent class or base class.

