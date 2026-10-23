# ### 3 · Build Logbook and independent state · 65 minutes

# Use ordinary loops, lists and dictionaries. Keep both classes in the practice file for this session.

# Write `Logbook()` with a new empty `self.flights` list created during each instance's initialization. Add:

# - `add_flight(flight)`: append the supplied Flight object.
# - `total_hours()`: return the sum of the stored flight durations; return zero for an empty logbook.
# - `hours_by_type()`: return a dictionary mapping each flight type to its total hours; return an empty dictionary when empty.

# Use this fixed dataset before changing any objects:

# | Date | Aircraft | Hours | Type |
# | --- | --- | --- | --- |
# | 2026-10-19 | C172 | 1.50 | training |
# | 2026-10-20 | PA28 | 2.00 | cross_country |
# | 2026-10-21 | C172 | 0.75 | training |

# Expected checks: total **4.25 hours**; training **2.25**; cross_country **2.00**; individual minutes **90, 120, 45**.

# Make a second empty logbook; adding to the first must leave the second empty. In a separate tiny broken example, put `flights = []` on the class, reproduce unwanted sharing, then repair it. Explain why creating a list inside each `__init__` fixes that bug.



class Logbook:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def total_hours(self):
        total = 0
        for flight in self.flights:
            total += flight.duration
        return total

    def hours_by_type(self):
        hbt = {}
        for flight in self.flights:
            flight_type = flight.flight_type

            if flight_type in hbt:
                hbt[flight_type] += flight.duration
            else:
                hbt[flight_type] = flight.duration

        return hbt

    
from recall import Flight

f1 = Flight("2026-10-19", "C172", 1.5, "training")
f2 = Flight("2026-10-20", "PA28", 2.0, "cross_country")
f3 = Flight("2026-10-21", "C172", 0.75, "training")
book = Logbook()
book.add_flight(f1)
book.add_flight(f2)
book.add_flight(f3)

print(f1.describe())
