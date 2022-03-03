#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. What is the concept of an abstract superclass?

# A common superclass for several subclasses.
# Factor up common behavior
# Define the methods they all respond to.
# Methods that subclasses should implement are declared abstract
# Instances of the subclasses are created, but no instances of the superclass



# In[4]:


#2. What happens when a class statement's top level contains a basic assignment statement?
# Basic assignment statement: An assignment statement gives a value to a variable. For example, ... the variable may be a simple name, or an indexed location in an array, or a field (instance variable) of an object, or a static field of a class; and. the expression must result in a value that is compatible with the type of the variable .
# If the target is an attribute reference: The primary expression in the reference is evaluated. It should yield an object with assignable attributes; if this is not the case, TypeError is raised. That object is then asked to assign the assigned object to the given attribute; if it cannot perform the assignment, it raises an exception (usually but not necessarily AttributeError).

# Note: If the object is a class instance and the attribute reference occurs on both sides of the assignment operator, the right-hand side expression, a.x can access either an instance attribute or (if no instance attribute exists) a class attribute. The left-hand side target a.x is always set as an instance attribute, creating it if necessary. Thus, the two occurrences of a.x do not necessarily refer to the same attribute: if the right-hand side expression refers to a class attribute, the left-hand side creates a new instance attribute as the target of the assignment:

class Cls:
    x = 3             # class variable
inst = Cls()
inst.x = inst.x + 1   # writes inst.x as 4 leaving Cls.x as 3
# This description does not necessarily apply to descriptor attributes, such as properties created with property().


# In[ ]:


#3. Why does a class need to manually call a superclass's __init__ method?

#super() in Single Inheritance
If you’re unfamiliar with object-oriented programming concepts, inheritance might be an unfamiliar term. Inheritance is a concept in object-oriented programming in which a class derives (or inherits) attributes and behaviors from another class without needing to implement them again.

For me at least, it’s easier to understand these concepts when looking at code, so let’s write classes describing some shapes:
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width
Here, there are two similar classes: Rectangle and Square.

You can use them as below:
class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length

 In this example, you have two shapes that are related to each other: a square is a special kind of rectangle. The code, however, doesn’t reflect that relationship and thus has code that is essentially repeated.

By using inheritance, you can reduce the amount of code you write while simultaneously reflecting the real-world relationship between rectangles and squares:
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
        
Here, you’ve used super() to call the __init__() of the Rectangle class, allowing you to use it in the Square class without repeating code. Below, the core functionality remains after making changes:

>>> square = Square(4)
>>> square.area()
16

In this example, Rectangle is the superclass, and Square is the subclass.

Because the Square and Rectangle .__init__() methods are so similar, you can simply call the superclass’s .__init__() method (Rectangle.__init__()) from that of Square by using super(). This sets the .length and .width attributes even though you just had to supply a single length parameter to the Square constructor.

When you run this, even though your Square class doesn’t explicitly implement it, the call to .area() will use the .area() method in the superclass and print 16. The Square class inherited .area() from the Rectangle class.


# In[ ]:


#4. How can you augment, instead of completely replacing, an inherited method?

Inheritance is designed to promote code reuse but can lead to the opposite result
Multiple inheritance allows us to keep the inheritance tree simple
Multiple inheritance leads to possible problems that are solved in Python through the MRO(Method Resolution Order).
Interfaces (either implicit or explicit) should be part of your design
Mixin classes are used to add simple changes to classes
Mixins are implemented in Python using multiple inheritance: they have great expressive power but require careful design
    
#MRO is a good solution that prevents ambiguity, but it leaves programmers with the responsibility of creating sensible inheritance trees. The algorithm helps to resolve complicated situations, but this doesn't mean we should create them in the first place. So, how can we leverage multiple inheritance without creating systems that are too complicated to grasp? Moreover, is it possible to use multiple inheritance to solve the problem of managing the double (or multiple) nature of an object, as in the previous example of a movable and resizeable shape?

#The solution comes from mixin classes: those are small classes that provide attributes but are not included in the standard inheritance tree, working more as "additions" to the current class than as proper ancestors.
    
#Python doesn't provide support for mixins with any dedicated language feature, so we use multiple inheritance to implement them. This clearly requires great discipline from the programmer, as it violates one of the main assumptions for mixins: their orthogonality to the inheritance tree. In Python, so-called mixins are classes that live in the normal inheritance tree, but they are kept small to avoid creating hierarchies that are too complicated for the programmer to grasp. In particular, mixins shouldn't have common ancestors other than object with the other parent classes.

#Let's have a look at a simple example

class GraphicalEntity:
    def __init__(self, pos_x, pos_y, size_x, size_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y


class ResizableMixin:
    def resize(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y


class ResizableGraphicalEntity(GraphicalEntity, ResizableMixin):
    pass

rge = ResizableGraphicalEntity(5, 4, 200, 300)
rge.resize(1000, 2000)

# Here, the class ResizableMixin doesn't inherit from GraphicalEntity, but directly from object, so ResizableGraphicalEntity gets from it just the resize method. As we said before, this simplifies the inheritance tree of ResizableGraphicalEntity and helps to reduce the risk of the diamond problem. It leaves us free to use GraphicalEntity as a parent for other classes without having to inherit methods that we don't want. Please remember that this happens because the classes are designed to avoid it, and not because of language features: the MRO algorithm just ensures that there will always be an unambiguous choice in case of multiple ancestors.

# Mixins cannot usually be too generic. After all, they are designed to add features to classes, but these new features often interact with other pre-existing features of the augmented class. In this case, the resize method interacts with the attributes size_x and size_y that have to be present in the object. Obviously, there are obviously examples of pure mixins, but since they would require no initialization their scope is definitely limited.


# In[ ]:


#5. How is the local scope of a class different from that of a function?
#Every block (code appearing between a { and } ) defines a new scope - the region in a program where a name, usually a variable, is visible and accessible. Although blocks can be nested arbitrarily deep, there are only three main or named levels of scope:

1. Local: inside a function
2. Global: outside all functions and classes
3. Class: inside a class (i.e., an attribute or a member variable)
#Programmers often classify variables by their scope: they define global variables in global scope, local variables in local scope, and class variables in class scope.

#Declaring a variable in a class (outside of a function): all class functions can access it (basically a public variable)

#Declaring a variable inside a function inside a class: only that function can access it (it's in that function's scope)

#Declaring a variable with self.(variable name) inside a function inside a class: all class functions can access it (how is this different from global (variable name)?)

#And since there is no private/protected, everything is public, so everything accessible from inside a class is accessible from outside the class.

