#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('Q1. What is the difference between __getattr__ and __getattribute__');get_ipython().run_line_magic('pinfo', '__getattribute__')

The __getattr__ and __getattribute__ operator overloading methods provide still
other ways to intercept attribute fetches for class instances. Like properties and descriptors, they allow us to insert code to be run automatically when attributes are accessed; as we’ll see, though, these two methods can be used in more general ways.
Attribute fetch interception comes in two flavors, coded with two different methods:
• __getattr__ is run for undefined attributes—that is, attributes not stored on an
instance or inherited from one of its classes.
• __getattribute__ is run for every attribute, so when using it you must be cautious
to avoid recursive loops by passing attribute accesses to a superclass.

__getattr__ and __getattribute__ Compared
To summarize the coding differences between __getattr__ and __getattribute__, the
following example uses both to implement three attributes—attr1 is a class attribute,
attr2 is an instance attribute, and attr3 is a virtual managed attribute computed when
fetched:
class GetAttr:
    attr1 = 1
    def __init__(self):
    self.attr2 = 2
    def __getattr__(self, attr): # On undefined attrs only
    print('get: ' + attr) # Not attr1: inherited from class
    return 3 # Not attr2: stored on instance
X = GetAttr()
print(X.attr1)
print(X.attr2)
print(X.attr3)
print('-'*40)
class GetAttribute(object): # (object) needed in 2.6 only
    attr1 = 1
    def __init__(self):
    self.attr2 = 2
    def __getattribute__(self, attr): # On all attr fetches
    print('get: ' + attr) # Use superclass to avoid looping here
    if attr == 'attr3':
    return 3
else:
    return object.__getattribute__(self, attr)
X = GetAttribute()
print(X.attr1)
print(X.attr2)
print(X.attr3)
When run, the __getattr__ version intercepts only attr3 accesses, because it is undefined. The __getattribute__ version, on the other hand, intercepts all attribute fetches
and must route those it does not manage to the superclass fetcher to avoid loops:
1
2
get: attr3
3
----------------------------------------
get: attr1
1
get: attr2
2
get: attr3
3
Although __getattribute__ can catch more attribute fetches than __getattr__, in practice they are often just variations on a theme—if attributes are not physically stored,
the two have the same effect.
The __getattr__ method is run for fetches of undefined attributes only—i.e., those
not present on an instance and not inherited from any of its classes. By contrast,
the __getattribute__ method is called for every attribute fetch, whether the attribute is defined or not. Because of this, code inside a __getattr__ can freely fetch
other attributes if they are defined, whereas __getattribute__ must use special code
for all such attribute fetches to avoid looping (it must route fetches to a superclass
to skip itself).


# In[ ]:


get_ipython().set_next_input('Q2. What is the difference between properties and descriptors');get_ipython().run_line_magic('pinfo', 'descriptors')

 Properties serve a specific role, while descriptors are more general. Properties define
get, set, and delete functions for a specific attribute; descriptors provide a class
with methods for these actions, too, but they provide extra flexibility to support
more arbitrary actions. In fact, properties are really a simple way to create a specific
kind of descriptor—one that runs functions on attribute accesses. Coding differs
too: a property is created with a built-in function, and a descriptor is coded with
a class; as such, descriptors can leverage all the usual OOP features of classes, such
as inheritance. Moreover, in addition to the instance’s state information, descriptors have local state of their own, so they can avoid name collisions in the instance.


# In[ ]:


get_ipython().set_next_input('Q3. What are the key differences in functionality between __getattr__ and __getattribute__, as well as properties and descriptors');get_ipython().run_line_magic('pinfo', 'descriptors')
The __getattr__ and __getattribute__ methods are more generic: they can be used
to catch arbitrarily many attributes. In contrast, each property or descriptor provides access interception for only one specific attribute—we can’t catch every attribute fetch with a single property or descriptor. On the other hand, properties
and descriptors handle both attribute fetch and assignment by design:
__getattr__ and __getattribute__ handle fetches only; to intercept assignments
as well, __setattr__ must also be coded. The implementation is also different:
__getattr__ and __getattribute__ are operator overloading methods, whereas
properties and descriptors are objects manually assigned to class attributes.

