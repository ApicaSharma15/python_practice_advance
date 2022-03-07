#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Q1. Does assigning a value to a string's indexed character violate Python's string immutability?

#In python, the string data types are immutable. Which means a string value cannot be updated. We can verify this by trying to update a part of the string which will led us to an error.

#Data types in python are either mutable (changeable) or immutable. the limitation of immutable types is that the data cannot be changed in places. The following data for example is not valid:
    
my_str = "Hi, My name is Rahul"
my_str[0]= h # Error 


#The second statement in the above example is invalid because it attempts to take the string created in the first statement and modify the data itself. As a result, python raises a TypeError exception. 
#But the following statements are valid :
    
my_str ="Hello"
my_str ="hello"

#These statements are valid because every time a completely new string is created, and the name my_str is reassigned.
# In python a variable is nothing more than a name , and it may be reused, over and over. Thats why these last statements might seem to violate immutability of strings but infact do not. 
# No existing string is altered in this last example; rather two different strings are created and the name my_str is reused.
# This behaviour follows from the nature of assignment in python and its lack of data declarations. You can use a name as often as you want.


# In[ ]:


#Q2. Does using the += operator to concatenate strings violate Python's string immutability? Why or why not?

#The string itself is immutable but the label can change. Assigning a new value to an existing variable is perfectly valid. Python does not have constants. This is independent from data type mutability
# Something is mutable only when we are able to change the values held in the memory location without changing the memory location itself.

The trick is: If you find that the memory location before and after the change are the same, it is mutable.

get_ipython().set_next_input('For example, list is mutable. How');get_ipython().run_line_magic('pinfo', 'How')

>> a = ['hello']
>> id(a)
139767295067632

# Now let's modify
#1
>> a[0] = "hello new"
>> a
['hello new']
Now that we have changed "a", let's see the location of a
>> id(a)
139767295067632
so it is the same as before. So we mutated a. So list is mutable.
get_ipython().set_next_input('A string is immutable. How do we prove it');get_ipython().run_line_magic('pinfo', 'it')

> a = "hello"
> a[0]
'h'
# Now let's modify it
> a[0] = 'n'
----------------------------------------------------------------------
we get

TypeError: 'str' object does not support item assignment

So we failed mutating the string. It means a string is immutable.

In you reassigning, you change the variable to point to a new location itself. Here you have not mutated the string, but mutating the variable itself. The following is what you are doing.

>> a = "hello"
>> id(a)
139767308749440
>> a ="world"
>> id(a)
139767293625808
id before and after reassignment is different, so it this proves that you are actually not mutating, but pointing the variable to new location. Which is not mutating that string, but mutating that variable.



# In[ ]:


#Q3. In Python, how many different ways are there to index a character?


#In Python, the elements of ordered sequences like strings or lists can be -individually- accessed through their indices. This can be achieved by providing the numerical index of the element we wish to extract from the sequence. Additionally, Python supports slicing that is a characteristic that lets us extract a subset of the original sequence object.
# Like most programming languages, Python offsets start at position 0 and end at position N-1, where N is defined to be the total length of the sequence. For instance, the total length of the string Hello is equal to 5 and each individual character can be accessed through indices 0 to 4

#Now you can programmatically access individual characters in the string, by providing the corresponding offset you wish to fetch, enclosed in square brackets:
    
my_string = 'Hello'
 print(my_string[0])
'H'
 print(my_string[2])
'l'
 print(my_string[3])
'l'

#It is also possible to access an element by providing a negative index that essentially corresponds to the index starting from the right of the sequence. The last item can be accessed through offset -1, the last but one through offset -2 and so on
#Technically when a negative offset is used, Python adds that offset to the length of the sequence in order to infer the exact position. For example, say we want to extract character e from the string my_string = 'Hello’ using a negative offset. Now the expression my_string[-4] will essentially be translated into my_string[len(my_string) — 4] which is equivalent to my_string[5 — 4] and my_string[1]that finally gives us the desired output:

my_string[-4]
'e'


# In[ ]:


get_ipython().set_next_input('Q4. What is the relationship between indexing and slicing');get_ipython().run_line_magic('pinfo', 'slicing')
#Two of the ways to extract data from strings include indexing and slicing. 

# Slicing is one form of indexing that allows us to infer an entire (sub)section of the original sequence rather than just a single item. To perform a slicing over a sequence in Python, you need to provide two offsets separated by a colon although in some cases you can define just one of the two, or even none 
# The first offset denotes the starting point and is inclusive while the second offset denotes the ending point but in contrast to the starting offset, it is non-inclusive.

    my_string = 'Hello'
    my_string[start:end]

#Therefore, when performing slicing Python will return a new object including all the elements starting from the lower index up to the position which is one less the upper index. As an example, consider a use-case where we need to take the first two elements of the string:
   my_string[0:2]
'He'

As I already mentioned, it is not mandatory to provide explicit offsets. When the starting offset is omitted, then its value will default to 0. On the other hand, when the ending offset is not provided, its default value will be equal to the length of the sequence. There are actually three different scenarios which are shown below:
my_string[0:]   # Omit ending offset
my_string[:-1]  # Omit starting offset
my_string[:]    # Omit both starting and ending offsets
Omitting the end offset
The first notation is typically useful when we want to chop off leading text. Say we want to get all but the first character of our string. We can do so by using the following notation
 my_string = 'Hello'
    my_string[1:]
'ello'
As we already mentioned, when the ending offset is omitted the length of the sequence will be used instead:
    my_string[1:] == my_string[1:len(my_string)]
True
Omitting start offset
Let’s assume that we now want all but the first character of our string. In this case, omitting the starting offset will do the trick:
    my_string = 'Hello'
    my_string[:-1]
'Hell'
Given that the lower bound is skipped, its value will default to 0:
    my_string[:-1] == my_string[0:-1]
True
Omitting both offsets
Slicing notation in Python allows us to omit both the starting and ending offsets.
    my_string = 'Hello'
    my_string[:] == my_string[0:len(my_string)]
True
Given that when lower and upper bounds are ignored will default to 0 and len(sequence) respectively you might be wondering whether this could be of any help or use. Well, this is a quick way to take a copy of the object as shown below
    my_string = 'Hello'
    my_string_copy = my_string[:]
Note that when this slicing technique will generated a different object that will be allocated to a different memory location. This doesn’t make any sort of difference for immutable object types like strings, however it is quite important to be aware of this when dealing with mutable object types such as lists. For more details on this, you can refer to my article Dynamic Typing in Python that discusses how objects are created and (properly) copied.
Extended slicing
Slicing expressions in Python come with a third index which is optional and when specified is used as a step. Obviously, when the step value is omitted it defaults to 1 which means that no element in the requested sequence sub-section will be skipped. The notation is shown below
[start:end:step]
As an example, consider that we have a string with the letters of the alphabet from which we want to extract every other item in it, between letters in positions 1 and 19:
    import string
    my_string = string.ascii_lowercase # 'abcdefg...'
    my_string[1:20:2]
'bdfhjlnprt'
Such notation can be used to replace list comprehensions. For instance, let’s say we want to get all the elements of a list that have an even index. A list comprehension that achieves this would be
    my_list = [100, 400, 34, 179, 0, 89, 121]
    [value for index, value in enumerate(my_list) if index % 2 == 0]
[100, 34, 0, 121]
In this occasion, slicing notation could make our code simpler and much more readable:
    my_list = [100, 400, 34, 179, 0, 89, 121]
    my_list[::2]
[100, 34, 0, 121]
Like start and end offsets, the step index can be a negative number. Technically this is useful when we want to reverse the order of the elements in an ordered sequence
    my_string = 'Hello'
    my_string[::-1]
'olleH'
In other words, when a negative step index is applied the effect of starting and ending offsets is reversed. To make this clear let’s jump into another example where we actually define all three possible offsets.
    import string
    my_string = string.ascii_lowercase # 'abcdefg...'
    my_string[20:10:-1]
'utsrqponml'
In the example above, we essentially create a new string from indices 11 to 20 in reversed order.


Indexing
The first item starts at offset 0
The last item ends at offset len(my_sequence) — 1
Negative indices indicate that the count will start backwards. Essentially it is being added to the length of the sequence. For example, my_string[-1] translates to my_string[len(my_string) — 1]
Slicing
The starting index (lower bound) is inclusive
The ending index (upper bound) is non-inclusive
When the starting index it omitted, it defaults to 0
When the ending index is omitted, it defaults to the length of the sequence
When both starting and ending indices are omitted, a copy of the original object is created — my_string[:]
The third index denotes the step
When the step index is omitted, it defaults to 1 (i.e. no element is skipped)
A negative step index helps us create reversed sequences (e.g. my_string[::-1] )


# In[ ]:


#Q5. What is an indexed character's exact data type? What is the data form of a slicing-generated substring?

#indexing returns a string — Python has no special type for a single character. It is just a string of length 1.
#In python substring is a sequence of characters within another string, In python, it is also referred to as the slicing of string. hence data type is also a string.


# In[ ]:


#Q6. What is the relationship between string and character "types" in Python?
In Python, Strings are arrays of bytes representing Unicode characters. However, Python does not have a character data type, a single character is simply a string with a length of 1. Square brackets can be used to access elements of the string.
Strings in Python can be created using single quotes or double quotes or even triple quotes. 
# Python Program for
# Creation of String

# Creating a String
# with single Quotes
String1 = 'Welcome to the Geeks World'
print("String with the use of Single Quotes: ")
print(String1)

# Creating a String
# with double Quotes
String1 = "I'm a Geek"
print("\nString with the use of Double Quotes: ")
print(String1)

# Creating a String
# with triple Quotes
String1 = '''I'm a Geek and I live in a world of "Geeks"'''
print("\nString with the use of Triple Quotes: ")
print(String1)

# Creating String with triple
# Quotes allows multiple lines
String1 = '''Geeks
			For
			Life'''
print("\nCreating a multiline String: ")
print(String1)


Accessing characters in Python
In Python, individual characters of a String can be accessed by using the method of Indexing. Indexing allows negative address references to access characters from the back of the String, e.g. -1 refers to the last character, -2 refers to the second last character, and so on. 

While accessing an index out of the range will cause an IndexError. Only Integers are allowed to be passed as an index, float or other types that will cause a TypeError. 
# Python Program to Access
# characters of String

String1 = "GeeksForGeeks"
print("Initial String: ")
print(String1)

# Printing First character
print("\nFirst character of String is: ")
print(String1[0])

# Printing Last character
print("\nLast character of String is: ")
print(String1[-1])

#A google search for "python str" should lead you to the official python.org string methods which lists all the str methods. Python does not have a separate character type. Instead an expression like s[8] returns a string-length-1 containing the character.


# In[ ]:



#Q7. Identify at least two operators and one method that allow you to combine one or more smaller strings to create a larger string.
Considering that strings are immutable , we construct new strings as follows:
    
    Once again the special nature of python assignment comes to the rescue. For example the following statements build the string "Big Bad John".
    

a_str ="Big"
a_str = a_str + "Bad"
a_str = a_str + "John"
These are perfectly valid statements. They resuse the name a_str, each time assigning a new string to the name. The end result is to create the following string:
    
"Big Bad John"

The following statements are also valid , and even if they seem to volate immutability , they actually do not. 
a_str = "Big"
a_str += "Bad"
a_str += "John"

This technique, of using +,= and += is to build strings, adequate for simpler cases involving a few objects. For example, you could build a string containing all the letters of the alphabet as follows, using the ord and chr functions 

n = ord('A')
s =''
for i in range (n,n+26):
    s += chr(i)
    
This example has the virtue of brevity. But it causes python to create entirely new strings in memory, over and over again.

A slightly better alternative is to use the join method.

separator_string.join(list)

This method joins together all the strings in list to form one large string. If this list has more than one element, the text of separator_string is placed betweeen each consecutive pair of strings. An empty list is a valid separator string: in that case, all the strings in the list are simply joined together. 
Use of join is usually more efficient at run-time than concatenation, although you probably wont see the difference in execution time unless there are a great many elements.

n = ord('A')
a_lst = []
for i in range (n, n+26):
    a_lst.append(chr(i))
s =''.join(a_lst) 


The join method concatenates all the strings in a_lst , a list of strings, into one large string. The separator string is empty in this case.

Here's a case in which the approach of using join is superior : Suppose you want to write a function that takes a list of names and prints them one at a time , nicely separated by commas. Here's the hard way to write the code:

def print_nice(a_lst):
    s =''
    for item in a_lst:
        s += item + ','
        if len (s) > 0:   # Get rid of trailing commas
            s = s[:-2]
            
        print(s)
        
Given this function definition, we call it on a list of strings
print_nice (['John', 'Paul', 'George', 'Rinku'])

This example prints the following: 
    John, aul, George, Rinku
    
Here's the version using the join method:

def print_nice(a_lst):
    print(','.join(a_lst) )
    
Thats quite a bit less code!


# In[ ]:



#Q8. What is the benefit of first checking the target string with in or not in before using the index method to find a substring?

The in or not in operators, although not limited to use with one-character strings, often are used that way. For example, the following statement statements test whether the first character of a string is a vowel :
    
s ='elephant'
if s[0] in 'aeiou':
    print ('First char is vowel.')
    
Conversely you could write a consonant test.
s ='Helephant'
if s[0] not in 'aeiou':
    print('First character is a consonant.')
    
One obvious drawback is that these letters do not correctly work for uppercase letters. One fix for that is that
s ='elephant'
if s[0] in 'aeiouAEIOU':
    print ('First char is vowel.') 

AND MODIFICATIONS AND EXAMPLES ARE MANY MORE. 


# In[ ]:


#Q9. Which operators and built-in string methods produce simple Boolean (true/false) results?

# Methods which began with the word "is" in their name - return either True or False. They are often used with Single character strings but can also be used on longer strings; in that case they return True if and only if every character in the string passes the test. 
There are a number of string methods that will return Boolean values:

Method	True if
str.isalnum()	String consists of only alphanumeric characters (no symbols)
str.isalpha()	String consists of only alphabetic characters (no symbols)
str.islower()	String’s alphabetic characters are all lower case
str.isnumeric()	String consists of only numeric characters
str.isspace()	String consists of only whitespace characters
str.istitle()	String is in title case
str.isupper()	String’s alphabetic characters are all upper case
Let’s review a couple of these in action:

number = "5"
letters = "abcdef"

print(number.isnumeric())
print(letters.isnumeric())

