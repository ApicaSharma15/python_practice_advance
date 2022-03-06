#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Q1. What is the purpose of the try statement?

## The try and except block in Python is used to catch and handle exceptions. Python executes code following the try statement as a “normal” part of the program. The code that follows the except statement is the program's response to any exceptions in the preceding try clause

Try and Except statement is used to handle these errors within our code in Python. The try block is used to check some code for errors i.e the code inside the try block will execute when there is no error in the program. Whereas the code inside the except block will execute whenever the program encounters some error in the preceding try block.
 

Syntax: 

try:
    # Some Code
except:
    # Executed if error in the
    # try block
How try() works? 
 

First, the try clause is executed i.e. the code between try and except clause.
If there is no exception, then only the try clause will run, except the clause is finished.
If any exception occurs, the try clause will be skipped and except clause will run.
If any exception occurs, but the except clause within the code doesn’t handle it, it is passed on to the outer try statements. If the exception is left unhandled, then the execution stops.
A try statement can have more than one except clause


# In[ ]:


#Q2. What are the two most popular try statement variations?

First, the try clause is executed i.e. the code between try and except clause.
If there is no exception, then only the try clause will run, except the clause is finished.
If any exception occurs, the try clause will be skipped and except clause will run.
If any exception occurs, but the except clause within the code doesn’t handle it, it is passed on to the outer try statements. If the exception is left unhandled, then the execution stops.
A try statement can have more than one except clause





# Python code to illustrate
# working of try()
def divide(x, y):
    try:
        # Floor Division : Gives only Fractional Part as Answer
        result = x // y
        print("Yeah ! Your answer is :", result)
except ZeroDivisionError:
    print("Sorry ! You are dividing by zero ")

# Look at parameters and note the working of Program
divide(3, 0)







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


#Q3. What is the purpose of the raise statement?
#The raise keyword is used to raise an exception. You can define what kind of error to raise, and the text to print to the user.

Example
Raise a TypeError if x is not an integer:

x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed")


# In[ ]:


#Q4. What does the assert statement do, and what other statement is it like?

# The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError. You can write a message to be written if the code returns False, check the example below.
x = "hello"

#if condition returns True, then nothing happens:

assert x == "hello"

#if condition returns False, AssertionError is raised:
assert x == "goodbye"


# The assert keyword is used when debugging code.
# Assertions in any programming language are the debugging tools that help in the smooth flow of code. Assertions are mainly assumptions that a programmer knows or always wants to be true and hence puts them in code, so that failure of these doesn’t allow the code to execute further. 

#In simpler terms, we can say that assertion is the boolean expression that checks if the statement is True or False. If the statement is true then it does nothing and continues the execution, but if the statement is False then it stops the execution of the program and throws an error.


# Python 3 code to demonstrate
# working of assert

# initializing number
a = 4
b = 0

# using assert to check for 0
print("The value of a / b is : ")
assert b != 0, "Zero Division Error"
print(a / b)


# In[ ]:


#Q5. What is the purpose of the with/as argument, and what other statement is it like?
The with statement in Python is used for resource management and exception handling. You'd most likely find it when working with file streams. For example, the statement ensures that the file stream process doesn't block other processes if an exception is raised, but terminates properly.

The code block below shows the try-finally approach to file stream resource management.

file = open('file-path', 'w') 
try: 
    file.write('Lorem ipsum') 
finally: 
    file.close() 
Normally, you’d want to use this method for writing to a file, but the with statement offers a cleaner approach:

with open('file-path', 'w') as file: 
    file.write('Lorem ipsum') 
The with statement simplifies our write process to just two lines.

It is also used in database CRUD processes. This example was taken from this site:

def get_all_songs():
    with sqlite3.connect('db/songs.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM songs ORDER BY id desc")
        all_songs = cursor.fetchall()
        return all_songs
Here, with is used to query an SQLite database and return its content.

