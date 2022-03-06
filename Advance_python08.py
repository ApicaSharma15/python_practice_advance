#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Q1. What are the two latest user-defined exception constraints in Python 3.X?

#Python throws errors and exceptions whenever code behaves abnormally & its execution stop abruptly. Python provides us tools to handle such scenarios by the help of exception handling method using try-except statements. Some standard exceptions which are found are include ArithmeticError, AssertionError, AttributeError, ImportError, etc.

#Creating a User-defined Exception class :
##Here we created a new exception class i.e. User_Error. Exceptions need to be derived from the built-in Exception class, either directly or indirectly. Let’s look at the given example which contains a constructor and display method within the given class

Example


# class MyError is extended from super class Exception
class User_Error(Exception):
   # Constructor method
   def __init__(self, value):
      self.value = value
   # __str__ display function
   def __str__(self):
      return(repr(self.value))
try:
   raise(User_Error("User defined error"))
   # Value of Exception is stored in error
except User_Error as error:
   print('A New Exception occured:',error.value)

##Creating a User-defined Exception class (Multiple Inheritance)
##Derived class Exceptions are created when a single module handles multiple several distinct errors. Here we created a base class for exceptions defined by that module. This base class is inherited by various user-defined class to handle different types of errors.

Example
 

# define Python user-defined exceptions
class Error(Exception):
   """Base class for other exceptions"""
   pass
class Dividebyzero(Error):
   """Raised when the input value is zero"""
   pass
try:
   i_num = int(input("Enter a number: "))
   if i_num ==0:
      raise Dividebyzero
except Dividebyzero:
   print("Input value is zero, try again!")
   print()
    
##Creating a User-defined Exception class (standard Exceptions)
##Runtime error is a built-in class which is raised whenever a generated error does not fall into mentioned categories. The program below explains how to use runtime error as base class and user-defined error as derived class.

Example
 

# User defined error
class Usererror(RuntimeError):
   def __init__(self, arg):
      self.args = arg
try:
   raise Usererror("userError")
except Usererror as e:
   print (e.args)


# In[ ]:


#Q2. How are class-based exceptions that have been raised matched to handlers?

Class-based exceptions are objects of different specific exception classes which can use attributes to supply additional information about the error type they represent. You can also pass additional specific details about a particular error to the object at runtime, when the object is generated. This is the information part of an exception.

Once an exception of a particular type or class is raised, the runtime looks for the first suitable handler by going first to the procedure where the exception occurred, and then by going up the call stack. When a suitable handler is found, the control flow proceeds with that handler’s code.

The handler should contain some code to resolve the error: to repair it, to abort some procedures or to end processing of the whole program-component, in which the error occurred. The appropriate handling of an exception depends on a thorough semantic analysis of the kind of error that occurred and its impact.

To do this, first figure out what the effect of an error is, then decide what the best reaction to it is, and only as a third step try to find out how you can implement the error handling.

## Class- based exceptions match by superclass relationships: naming a superclass in an exception handler will catch instances of that class, as well as instances of any of its sub-classes lower in the class-tree. Because of this you can think of superclasses as general exception categories and subclasses as more specific types of exceptions within those categories. 


# In[ ]:


#Q3. Describe two methods for attaching context information to exception artefacts.

## you can attach context information to class-based exceptions by filling out instance attributtes in the instance object raised, usually in a custom class constructor. For simpler needs, built-in exception superclasses provide a constructor that stores its arguments on the instance automatically(in the attribute args). 
## in exception handlers, you list a variable to be assigned to the raised instance then go through this name to access attached state informtion and call any methods defined in the class 


# In[ ]:


#Q4. Describe two methods for specifying the text of an exception object's error message.

# The error message text in class-based exceptions can be specified with a custom __str__ operator overloading method. For simpler needs, buuilt -in exception superclasses automatically display anything you pass to the class constructor. Operations like print and str automatically fetch the display string of an exception object when is it printed either explicitly or as a part of an error message. 


# In[ ]:


#Q5. Why do you no longer use string-based exceptions?

# Because Guido said so - they have been removed from both python 2.6 and python 3.0
# There are good reasons for this : string based exceptions did not support categories, state information , or behaviour inheritance in the way class-based exceptions do .
# In practice, this made string based exceptions easier to use at first, when programs were small, but more complex to use as programs grew larger. 

