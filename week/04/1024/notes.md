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
`def __init__(self, make, model, year):`
this under the `ElectricCar` class takes in the information required to make an instance under the car class. 
The `super().__init__(make, model, year)` is a special function that helps Python make connections between the Parent and Child Class. Specifically it tells Python to call the init method from ElectricCar's parent class which gives the ElectricCar's instance all the attributes of its parent class. 


Inheiritance in Python 2.7 is a little bit different to call: 
```py
class Car(object):
# we define the parent class by using the object syntax as well
    def __init__(self, make, model, year):
        ---snip---
    
class ElectricCar(Car):
    def __init__(self, make, model, year)
        super(ElectricCar,self).__init__(make,model,year) 
# here super needs two arguements: a reference to the child class and the self object
    ---snip---
```


Once we have a child class that inheirits from a parent class we can build out methods to differentiate the child class from the parent. 


we can override a method in the parent class that doesnt fit what we are trying to model with the child class. Say the `Car` class had a `fill_gas_tank()` method that is meaningless within the `ElectricCar` class. All we need to do to override it is:
1. state the method under the `ElectricCar` class
2. give Python a workaround whenever someone calls the `fill_gas_tank` method as an instance of the `ElectricCar` class

Say, for instance, we start adding more and more to the ElectricCar class and it is growing to be a large class. The smart thing to do would be to split it up. Say we talk about the battery a lot. Lets model what that would look like below:

```py
class ElectricCar(Car):
    """Represents aspects of cars specific to electric vehicles"""
    def __init__(self, make, model, year): 
# takes the information required to make an instance under the car class
        """initialize attributes of the parent class"""
        super().__init__(make,model,year)
# this tells Python to call the child's parent class so we can have all the attributes of the parent class
        self.battery = Battery()
    
class Battery():
    """A simple attempt at modeling a battery for an electric car"""
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size
    def describe_battery(self):
            """Print a statement describing the battery size"""
            print("This car has a " + str(self.battery_size) + " -kWh battery.")
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


my_tesla = ElectricCar('tesla', 'model s', 2016)
# my_tesla.battery.battery_size = 85
print(my_tesla.get_descriptive_name())
my_tesla.battery.get_range()
```

So what we did here was we defined a new class named Battery that doesnt inherit from any other class. Because of this line: `self.battery = Battery()` under the ElectricCars init method. Every time there is an instance of ElectricCar formed, a Battery instance is formed as well. We tap into the methods under the Battery class with the self.battery.method and also for variables reassigning it would be self.battery.variable as stated above. All because `self.battery = Battery()`

