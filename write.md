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

An object is an instance of a class. We can take the `Parrot` class defined above, and use it to create an object or instance of it.

````
obj = Person()

````

### Class Variable
---
Class variables are defined within the class construction. Because they are owned by the class itself, class variables are shared by all instances of the class. 

````
class Person:
    country = "Bangladesh"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
obj = Person("Dedar",20)

````
Here country is a class variable.

### Instance Variable 
---
Instance variables are owned by instances of the class. This means that for each object or instance of a class, the instance variables are different.

Unlike class variables, instance variables are defined within methods.

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


### 