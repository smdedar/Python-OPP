### Class
---
A class is a blueprint for the object. 

Classes are like a blueprint or a prototype that need to  define to use or to create objects.

````
class Person:
    pass

````


### Object
---
An object (instance) is an instantiation of a class. When class is defined, only the description for the object is defined. Therefore, no memory or storage is allocated.

An object is an instance of a class. We can take the `Person` class defined above, and use it to create an object or instance of it.

````
obj = Person()

````

### Class Attribute
---
Class variables are defined within the class construction. Because they are owned by the class itself, class variables are shared by all instances of the class. 

Class attributes belong to the class itself they will be shared by all the instances. Such attributes are defined in the class body parts usually at the top

````
class Person:
    country = "Bangladesh"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
obj = Person("Dedar",20)

````
Here country is a class variable.

### Instance Attribute
---
Instance variables are owned by instances of the class. This means that for each object or instance of a class, the instance variables are different.

Unlike class variables, instance variables are defined within methods.

Unlike class attributes, instance attributes are not shared by objects. Every object has its own copy of the instance attribute (In case of class attributes all object refer to single copy).

````
class Person:
    country = "Bangladesh"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
obj = Person("Dedar",20)

````
Here, sentence name is instance variable





### Attribute
---
Characteristic of an object.

Attributes are the variables that belong to a class (can be of any data type)

````
class Person:
    country = "Bangladesh"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
obj = Person("Dedar",20)

````




### Method
---
Method is a special kind of function that is defined inside the class

Methods are functions defined inside the body of a class. They are used to define the behaviors of an object.

````
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def gender(self,gender):
        print(f'Person Name is {self.name}. Age {self.age} & Gender {gender}')

obj = Person("Dedar",20)

obj.gender("Male")

````
In the above program, we define one  method i.e gender()


### Constructor Method
---
The constructor method is used to initialize data. It is run as soon as an object of a class is instantiated. Also known as the `__init__` method.

````
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
````


### Inheritance
---
Inheritance is a way of creating a new class for using details of an existing class without modifying it. The newly formed class is a derived class (or child class). Similarly, the existing class is a base class (or parent class).

By using inheritance, we can create a class which uses all the properties and behavior of another class. The new class is known as a derived class or child class, and the one whose properties are acquired is known as a base class or parent class.

It provides the re-usability of the code.

````



````


### Polymorphism
---
 The word polymorphism means having many forms. In programming, polymorphism means same function name (but different signatures) being uses for different types.


````
# A simple Python function to demonstrate 
# Polymorphism 

def add(x, y, z = 0): 
	return x + y+z 

# Driver code 
print(add(2, 3)) 
print(add(2, 3, 4)) 

````


### Encapsulation

Encapsulation is also an essential aspect of object-oriented programming. It is used to restrict access to methods and variables. In encapsulation, code and data are wrapped together within a single unit from being modified by accident.

Using OOP in Python, we can restrict access to methods and variables. This prevents data from direct modification which is called encapsulation. In Python, we denote private attributes using underscore as the prefix i.e single _ or double __

````

````

### Data Abstraction

Data abstraction and encapsulation both are often used as synonyms. Both are nearly synonyms because data abstraction is achieved through encapsulation.

Abstraction is used to hide internal details and show only functionalities. Abstracting something means to give names to things so that the name captures the core of what a function or a whole program does.

