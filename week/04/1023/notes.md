# Inheiritance Day

we dont have to start all the way over with every class we make. We can use *inheiritance*. When one class inheirits from the other it automatically takes on all the attributes and methods of the parent class. The child class inheirits every attributeand method from its parent classbut is also free to define new attributes and methods of its own. 

The first task Python has when creating an instance from a child class is to assign values to all attributes in the parent class. A child class is a specialized version of the parent class, lets model inheiritance with a Car class and an Electric car class

```py
class Car:
    """ a simple attempt to model a car"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = int(year)
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
                self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    """Represents aspects of cars specific to electric vehicles"""
    def __init__(self, make, model, year):
        """initialize attributes of the parent class"""
        super().__init__(make,model,year)

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
```

When we make a child class, the parent class must: 
1. be in the same file
2. appear before the child class
3. be included in parenthesis as we define the child class

consider the following:
`    def __init__(self, make, model, year):`
this under the `ElectricCar` class takes in the information required to make an instance under the car class. 
The `super().__init__(make, model, year)` is a special function that helps Python make connections between the Parent and Child Class. Specifically it tells Python to call the init method from ElectricCar's parent class which gives the ElectricCar's instance all the attributes of its parent class. 
