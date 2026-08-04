Python Basics
List: What is a list, and when would you use one in Python?
A lists is a mutable collection. You Use it when need it store or change the stored  items.
Tuple: How is a tuple different from a list?
Cause a tuple is immutable so no changes can be added unlike a list with is mutablecan add to it.
Set: What makes a set different from a list?
A set stores items unordered and stores items to. 
Mutable: What does it mean if an object is mutable?
It can be changed after it is created.
Immutable: What does it mean if an object is immutable?
It cannot be changed after it was made

Functions & Dictionary Methods
len(): What does the len() function return?
Returns the number of items in an object, such as a list, tuple, string, dictionary, or set.

.get(): Why would you use the .get() method with a dictionary?
Used with a dictionary to safely get the value for a key. If the key does not exist, it returns None (or a default value you provide) instead of causing an error.
.length(): Is .length() a valid Python method? If not, what should you 
use instead?
No, .length() is not a valid Python method. Use the len() function instead to find the number of items in an object.
.keys(): What information does the .keys() method return?
Returns a view of all the keys in a dictionary.
.values(): What information does the .values() method return?
Returns a view of all the values stored in a dictionary.


List Methods
.remove(): What does the .remove() method do to a list?it lets you change the list or get information from it.
.pop(): How is .pop() different from .remove()?
both remove items from a list, but they remove them in different ways.
.sort(): What happens when you use .sort() on a list?the .sort method arranges the elements of a list in an ascending order by default.it modifies the original list instead of creating a new one
.append(): What does the .append() method do?it adds one item to the end of the list.
.insert(): How is .insert() different from .append()?they both add elements to a list they different in where the new element are placed.

Object-Oriented Programming (OOP)
Class: What is a class in Python?A class is a blueprint or template for creating objects.
Object: What is an object, and how is it related to a class?An object is a specific instance of a class. A class is the blueprint, and an object is something created from that blueprint.
Abstraction: What is abstraction, and why is it useful?
Abstraction is the process of hiding complex internal details to focus only on essential features, making it useful because it reduces information overload, simplifies system use, and improves code maintenance.
Encapsulation: How does encapsulation help protect an object's data?
Encapsulation protects an object's data by restricting direct access to its internal state and forcing all interactions to occur through a well-defined public interface.
Inheritance: What is inheritance, and why is it useful?
Inheritance is a core idea in Object-Oriented Programming where a new class (child) takes the traits and actions of an older class (parent). 
Polymorphism: How can different classes use the same method name but produce different results?
Different classes use the same method name to produce different results through a core Object-Oriented Programming (OOP) concept called polymorphism, which allows a single interface to represent different underlying forms.
Constructor: What is a constructor (__init__()), and when is it automatically called?
A constructor is a special function in a class that creates an object and sets its first values. It is named __init__() in Python. It is automatically called right when you make a new object from that class.



Challenge Questions
Which Python collection type cannot be changed after it is created?
A tuple can not be changed after being made because it’s mutable.
Which collection automatically removes duplicate values?
A set is a collection type that automatically removes duplicate values by storing only unique items. (Google A.I.)
What is the difference between a list and a dictionary?
A list is an ordered group of items accessed by number numbers, a dictionary is a collection of key-value pairs accessed by unique names, and both are mutable data tools. (Google A.I.)
Which list method would you use to add an item to the end of a list?
To add an item to the end of a list in Python, you use the append() method. (Google A.I.)
Which dictionary method would you use to safely retrieve a value by its key?
To safely retrieve a value by its key from a dictionary, you should use the get() method. (Google A.I.)
What is the difference between a class and an object?
The main difference is that a class is a blueprint or template used to define data structures, while an object is a concrete instance created from that blueprint that exists in memory. (Google A.I.)
How do inheritance and polymorphism work together in object-oriented programming?
Inheritance and polymorphism work together by using a parent class to establish a shared structural blueprint (inheritance) while allowing child classes to override specific behaviors with their own implementations (polymorphism). (Google A.I.)
Why are constructors important when creating objects?
Constructors are important because they initialize objects, enforce valid states, and prevent errors by setting up starting values automatically.(Google A.I.)
