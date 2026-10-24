# 65 min inheritance practice: build a separate Vehicle(make, hourly_cost) with operating_cost(hours) and describe().
#  Build Truck(make, hourly_cost, payload_kg) as a child. Call super().__init__(), add payload as a child attribute, 
# inherit the cost method and override describe(). Create a Vehicle and two Trucks with different values. 
# Verify that each Truck uses its own data. Then change one Truck's hourly cost and explain which results change.
#  Describe which method is inherited and which is overridden.

class Vehicle():
    def __init__(self, make, hourly_cost, hours):
        self.make = make.title()
        self.hourly_cost = float(hourly_cost)
        self.hours = float(hours)

    def day_cost(self):
        return self.hours*self.hourly_cost

    def describe(self):
        print(f"This is a {self.make} with the day rate of {self.day_cost()} sheckles for {self.hours} hours")

class Truck(Vehicle):
    def __init__(self, make, hourly_cost, hours, payload):
        super().__init__(make,hourly_cost, hours)
        self.payload = int(payload)
    def describe(self): # overridden
        print(f"This is a {self.make} with a towing capacity of {self.payload} lbs.\nThe day rate is {self.day_cost()} sheckles for {self.hours} hours.") 
        #day_cost in this print statement is inheirited




my_truck = Truck('ford-F150', 15, 10, 2000)
my_truck.describe()
my_car = Vehicle('toyota corrolla', 10, 10)
my_car.describe()
your_truck = Truck('chevy silverado', 20, 10, 4000)
your_truck.describe()