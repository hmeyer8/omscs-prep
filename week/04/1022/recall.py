# Flight(date, aircraft, duration, flight_type="training")
# duration measured consistently in **hours**.

# - Store the supplied values as instance attributes.
# - Give each instance a default `reviewed=False` attribute.
# - Add `duration_minutes()` returning a number and `describe()` returning a useful string.
# - Create three flights. Change one flight's duration and reviewed flag; check the other flights retain their own values.
# - Explain what class, instance, attribute, method, `self` and `__init__` mean using your code.

class Flight(): # class means the general family of objects that will be made via instances. 
    def __init__(self, date, aircraft, duration, flight_type = "training"): # the variables initially given to each object
        self.date = date
        self.aircraft = aircraft
        self.duration = float(duration)
        self.flight_type = flight_type # default variables
        self.reviewed = False

    def duration_minutes(self): # each method defines the behavior that you call
        out = self.duration *60 # self pulls the data initally given in the creation of the instance
        return out
    
    def describe(self):
        print(f"My {self.aircraft.title()} has {self.duration} hours or {self.duration_minutes()} minutes.") 
        if self.reviewed == True:
            print("This listing has been reviewed")
        else: print("This listing has not been reviewed")
piper = Flight('1994', 'piper', 267.873)
piper.describe()
piper.duration = 100
piper.reviewed = True
piper.describe()