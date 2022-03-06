#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Q1. Describe three applications for exception processing.

# Error in Python can be of two types i.e. Syntax errors and Exceptions. Errors are the problems in a program due to which the program will stop the execution. On the other hand, exceptions are raised when some internal events occur which changes the normal flow of the program. 
# Exceptions: Exceptions are raised when the program is syntactically correct, but the code resulted in an error. This error does not stop the execution of the program, however, it changes the normal flow of the program.
# Try and except statements are used to catch and handle exceptions in Python. Statements that can raise exceptions are kept inside the try clause and the statements that handle the exception are written inside except clause.

# Example: Let us try to access the array element whose index is out of bound and handle the corresponding exception.

# Python program to handle simple runtime error
#Python 3

a = [1, 2, 3]
try:
    print ("Second element = %d" %(a[1]))

# Throws error since there are only 3 elements in array
    print ("Fourth element = %d" %(a[3]))

except:
    print ("An error occurred")
#In the above example, the statements that can cause the error are placed inside the try statement (second print statement in our case). The second print statement tries to access the fourth element of the list which is not there and this throws an exception. This exception is then caught by the except statement.

## Catching Specific Exception
## A try statement can have more than one except clause, to specify handlers for different exceptions. Please note that at most one handler will be executed. For example, we can add IndexError in the above code. The general syntax for adding specific exceptions are – 
# Program to handle multiple errors with one
# except statement
# Python 3

def fun(a):
    if a < 4:

# throws ZeroDivisionError for a = 3
       b = a/(a-3)

# throws NameError if a >= 4
print("Value of b = ", b)

try:
    fun(3)
    fun(5)

# note that braces () are necessary here for
# multiple exceptions
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")
##The output above is so because as soon as python tries to access the value of b, NameError occurs. 

###Try with Else Clause
###In python, you can also use the else clause on the try-except block which must be present after all the except clauses. The code enters the else block only if the try clause does not raise an exception.

###Example: Try with else clause

# Program to depict else clause with try-except
# Python 3
# Function which returns a/b
def AbyB(a , b):
try:
    c = ((a+b) / (a-b))
except ZeroDivisionError:
    print ("a/b result in 0")
else:
    print (c)

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

####Raising Exception
####The raise statement allows the programmer to force a specific exception to occur. The sole argument in raise indicates the exception to be raised. This must be either an exception instance or an exception class (a class that derives from Exception).
# Program to depict Raising Exception

try:
    raise NameError("Hi there") # Raise Error
except NameError:
    print ("An exception")
    raise # To determine whether the exception was raised or not
####The output of the above code will simply line printed as “An exception” but a Runtime error will also occur in the last due to the raise statement in the last line.


# In[ ]:


#Q2. What happens if you don't do something extra to treat an exception?


## When an exception occurred, if you don’t handle it, the program terminates abruptly and the code past the line that caused the exception will not get executed.

The Tragic Crash of Flight AF447 Shows the Unlikely but Catastrophic Consequences of Automation


# In[ ]:


#Q3. What are your options for recovering from an exception in your script?

#Try and except statements are used to catch and handle exceptions in Python. Statements that can raise exceptions are kept inside the try clause and the statements that handle the exception are written inside except clause.
# Exceptions are the conditions that occur at runtime and may cause the termination of the program. But they are recoverable using try and catch  keywords.
First, the try clause is executed i.e. the code between try and except clause.
If there is no exception, then only the try clause will run, except the clause is finished.
If any exception occurs, the try clause will be skipped and except clause will run.
If any exception occurs, but the except clause within the code doesn’t handle it, it is passed on to the outer try statements. If the exception is left unhandled, then the execution stops.
A try statement can have more than one except clause
Python Exception Handling Mechanism
Exception handling is managed by the following 4 keywords:

try
catch
finally
throw
# Finally Keyword in Python
# Python provides a keyword finally, which is always executed after the try and except blocks. The final block always executes after normal termination of try block or after try block terminates due to some exceptions.
# Python program to demonstrate finally

# No exception Exception raised in try block
try:
    k = 5//0 # raises divide by zero exception.
    print(k)

# handles zerodivision exception	
except ZeroDivisionError:
    print("Can't divide by zero")

finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')
 


# In[ ]:


#Q4. Describe two methods for triggering exceptions in your script.

An unhandled exception displays an error message and the program suddenly crashes. To avoid such a scenario, there are two methods to handle Python exceptions:

Try – This method catches the exceptions raised by the program
Raise – Triggers an exception manually using custom exceptions
An exception is an error which happens at the time of execution of a program. However, while running a program, Python generates an exception that should be handled to avoid your program to crash. In Python language, exceptions trigger automatically on errors, or they can be triggered and intercepted by your code.
try:

     x = int(input(“Enter a positive integer: “))

if x <= 0:

         raise ValueError(“It is not a positive number!”)

except ValueError as val_e:

    print(val_e)


# In[ ]:


#Q5. Identify two methods for specifying actions to be executed at termination time, regardless of whether or not an exception exists.

##The optional else clause contains codes to be executed if no exception occurs. 
##The optional finally block contains codes to be executed irrespective of whether an exception occurs or not.
try:
    print('try block')
    x=int(input('Enter a number: '))
    y=int(input('Enter another number: '))
    z=x/y
except ZeroDivisionError:
    print("except ZeroDivisionError block")
    print("Division by 0 not accepted")
else:
    print("else block")
    print("Division = ", z)
finally:
    print("finally block")
    x=0
    y=0
print ("Out of try, except, else and finally blocks." )

