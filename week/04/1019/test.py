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

# my_dog = Dog('enny', 2)
# print("My dog's name is " + my_dog.name.title() + ".")
# print("My dog is " + str(my_dog.age) + " years old.")

# my_dog.sit()


class User():
    def __init__(self, first_name, last_name, height, weight):
        self.first_name = first_name
        self.last_name = last_name
        self.height = height
        self.weight = weight

    def describe_user(self):
        print(self.first_name.title() + " " + self.last_name.title() + 
              " is a " + str(self.height) + " foot " + str(self.weight) + 
              " pound man eating machine")


# tim = User('timmy', 'boy', 3, 50)
# tim.describe_user()

class Car():
    "a simple attempt at representing a car"
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def descriptive_title(self):
        long_name = str(self.year) + " " + str(self.make) + " " + str(self.model)
        return long_name.title()
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
my_new_car = Car('audi', 'r8', 2015)
print(my_new_car.descriptive_title())
print(my_new_car.read_odometer())

