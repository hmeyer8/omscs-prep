# 1019: 

### Learn:
     PCC ch 9: creating a class, an instance, __init__, attributes, and self; Tutorial 9.3 as reference
### Build: 
    Write an ordinary Flight class. Create three flights with different values. Add a method returning a description and another returning minutes. Do two short chapter exercises about creating instances.
### Evidence we are ready for the next day: 
    Explain the class versus one instance; trace each argument into an attribute; show why the methods return values.


## Learn Block:

Instantation - making an object from a class

Knowing logic behind classes will train you to think logically so you can write programs that effectively address almost any problem we encounter. 

First we are going to create a dog class. Not one dog but any dog. Two pieces of information: name and age. Two behaviors: sit and roll over goes into out dog class because theyre common in most dogs. 
The class tells python how to make an object representing a dog. 
After this class is written, we will use it to make individual instances which would represent one specific dog. 

```py
class Dog(): # capitol letter means class. 
    #Also parenthesis are empty because we are building this class from scratch.
    """A simple attempt to model a dog""" # doc string for this class
    #python runs the init method automatically when we create a new instance from the Dog class
    def __init__(self, name, age): # a function that belongs to a class is a method
        # self parameter is required in the method definition and must come first
        """ initialize name and age attributes"""
        self.name = name
        self.age = age

        # when we make an instance of Dog, we dont need to do Dog(self,"Benny", 2)
        # self is automatically passed so we just have do to Dog("Tommy", 2)
        # any variable prefixed with selfis available to every method in the class
        #      we will also be able to access these variables in instances of clases

    def sit(self): # since these methods dont need any other information, we just define with one parameter self
        """Simulate a dog sitting in response to a command"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """simulate rolling over in response to a command"""
        print(self.name.title() + " rolled over!")
```
Lets think of a class as a set of instrictions for how to make an instance
The class Dog is a set of instructions that tells Python how to make individual instances representing dogs

Lets make specific instances:
```py
my_dog = Dog('benny', 2)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
```
when we tell Python `my_dog = Dog('Benny', 2)` it calls the __init__() method in Dog with the arguements 'Benny' and 2. The init method creates an instance representing the particular dog and sets the name and age attributes with the inputs we gave it. 
the __init__() method has no explicit return statement but Python automatically returns an instance representing this dog where we store that instance in `my_dog`
We can ususally assume a capitalized name like Dog refers to a class and a lowercased name refers to an instance

### accessing attributes: 

to access the attributes in the instance `my_dog` we use dot notation. 
Here you can see the print at the bottom showing the `.make`
```py
class Car():
    "a simple attempt at representing a car"
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def descriptive_title(self):
        long_name = str(self.year) + " " + str(self.make) + " " + str(self.model)
        return long_name.title()

my_new_car = Car('audi', 'r8', 2015)
print(my_new_car.descriptive_title())
print(my_new_car.make)
```

