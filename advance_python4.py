#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Q1. Which two operator overloading methods can you use in your classes to support iteration?

The __iter__ returns the iterator object and is implicitly called at the start of loops. 
The __next__ method returns the next value and is implicitly called at each loop increment.

 __next__ raises a StopIteration exception when there are no more value to return, which is implicitly captured by looping constructs to stop iterating.
class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high
 
    def __iter__(self):
        return self
 
    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1
 
 
for num in Counter(5, 15):
    print(num)
 


# In[ ]:


#Q2. In what contexts do the two operator overloading methods manage printing?

Iterators are objects that can be iterated on, which means that the user can go over their values one by one. In Python, an iterator is an object used to iterate across iterable objects such as lists, tuples, dicts, and sets. The iter() method is used to initialize the iterator object. Iteration is accomplished through the usage of the next() method.

Python iterator implements the iterator protocol, which includes two special methods: __iter__() and __next__().
    
The __iter__() method – returns an iterator object. This is required in order to use containers and iterators with the for and in statements.
The __next__() method – This function returns the sequence’s next item. If no more items are found, throw the StopIteration exception.
Example


class Squares:
    def __init__(self, length):
        self.length = length
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.length:
            raise StopIteration

        self.current += 1
        return self.current ** 2

square_num = Squares(5)

for sq in square_num:
    print(sq)

print(next(square_num))

#output
1
4
9
16
25
Traceback (most recent call last):
File "", line 21, in 
File "", line 11, in __next__
StopIteration

Explanation

In the __init__ method, we first establish the length and current attributes, where the length attribute defines the number of square numbers that the class should return. And the current attribute keeps track of the integer that is currently in use. The __iter__ method, which returns the self object, is then implemented. The __next__ method, which returns the next square number, is implemented in the third phase. If the number of square numbers returned exceeds the length, the __next__ method throws the StopIteration exception.


# In[ ]:


#Q3. In a class, how do you intercept slice operations?

The __getitem__ method is used for accessing list items, array elements, dictionary entries etc. slice is a constructor in Python that creates slice object to represent set of indices that the range(start, stop, step) specifies. __getitem__ method can be implement in a class, and the behavior of slicing can be defined inside it.

Syntax:

__getitem__(slice(start, stop, step))
Parameter:

slice() : constructor to create slice object.
start: An integer number specifying start index.It is optional and default is 0.
stop: An integer number specifying end index.
step: An integer number specifying the step of slicing. It is optional and
default is 1.

class Demo:
    def __getitem__(self, key):

# print a[1], a[1, 2],
# a[1, 2, 3]
print(key)
return key
a = Demo()

# => slice 1
a[1]

# => slice(1, 2)
a[1, 2]

# => (1, 2, 3)
a[1, 2, 3]


#Output

1
(1, 2) 
(1, 2, 3)
#Explanation:
#The class demo has the __getitem__ method, slicing is comma-separated. Key prints the sliced object which is passed in class through variable a.


# In[ ]:


#Q4. In a class, how do you capture in-place addition?

Python in its definition provides methods to perform inplace operations, i.e doing assignment and computation in a single statement using “operator” module. For example,

x += y is equivalent to x = operator.iadd(x, y) 
Some Important Inplace operations :

1. iadd() :- This function is used to assign and add the current value. This operation does “a+=b” operation. Assigning is not performed in case of immutable containers, such as strings, numbers and tuples.

2. iconcat() :- This function is used to concat one string at end of second
3. isub() :- This function is used to assign and subtract the current value. This operation does “a-=b” operation. Assigning is not performed in case of immutable containers, such as strings, numbers and tuples.

4. imul() :- This function is used to assign and multiply the current value. This operation does “a*=b” operation. Assigning is not performed in case of immutable containers, such as strings, numbers and tuples.
5. itruediv() :- This function is used to assign and divide the current value. This operation does “a/=b” operation. Assigning is not performed in case of immutable containers, such as strings, numbers and tuples.

6. imod() :- This function is used to assign and return remainder . This operation does “a%=b” operation. Assigning is not performed in case of immutable containers, such as strings, numbers and tuples.

#example for in-place add operator in class
class Adder(object):
        def __init__(self, num=0):
            self.num = num

        def __iadd__(self, other):
            print 'in __iadd__', other
            self.num = self.num + other
            return self.num
    
a = Adder(2)
a += 3
in __iadd__ 3
a
5


# In[ ]:


#Q5. When is it appropriate to use operator overloading?
#The operator overloading in Python means provide extended meaning beyond their predefined operational meaning. Such as, we use the "+" operator for adding two integers as well as joining two strings or merging two lists. We can achieve this as the "+" operator is overloaded by the "int" class and "str" class.

#Python magic methods or special functions for operator overloading
Binary Operators:
Operator	Magic Method
+	__add__(self, other)
–	__sub__(self, other)
*	__mul__(self, other)
__truediv__((self,, other))
(/, __floordiv__(self,, other))
get_ipython().run_line_magic('__mod__', '(self, other)')
**	__pow__(self, other)
>>	__rshift__(self, other)
<<	__lshift__(self, other)
&	__and__(self, other)
|	__or__(self, other)
^	__xor__(self, other)
Comparison Operators :
Operator	Magic Method
<	__lt__(self, other)
>	__gt__(self, other)
<=	__le__(self, other)
>=	__ge__(self, other)
==	__eq__(self, other)
get_ipython().system('=\t__ne__(self, other)')
Assignment Operators :
Operator	Magic Method
-=	__isub__(self, other)
+=	__iadd__(self, other)
*=	__imul__(self, other)
(=, __idiv__(self,, other))
(/=, __ifloordiv__(self,, other))
get_ipython().run_line_magic('=\t__imod__(self,', 'other)')
**=	__ipow__(self, other)
>>=	__irshift__(self, other)
<<=	__ilshift__(self, other)
&=	__iand__(self, other)
|=	__ior__(self, other)
^=	__ixor__(self, other)
Unary Operators :
Operator	Magic Method
–	__neg__(self)
+	__pos__(self)
~	__invert__(self)
Note: It is not possible to change the number of operands of an operator. For ex. you cannot overload a unary operator as a binary operator. The following code will throw a syntax error.
    
# Python program which attempts to
# overload ~ operator as binary operator

class A:
    def __init__(self, a):
        self.a = a

# Overloading ~ operator, but with two operands
def __invert__(self, other):
    return "This is the ~ operator, overloaded as binary operator."


ob1 = A(2)
ob2 = A(3)

print(ob1~ob2)
    

