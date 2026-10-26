# recall.py | October 26 | 10 minutes
# Close notes, old code and AI. No answers included.

# --------------------------------------------------
# Rebuild Flight and Logbook
# --------------------------------------------------
# Write Flight(hours, flight_type):
# - Store hours as a float and store flight_type.
#
# Write Logbook():
# - Each instance starts with its own empty flights list.
# - add_flight(flight): store the supplied Flight object.
# - total_hours(): RETURN the total using an ordinary loop.
# - An empty logbook should return zero.
#
# Use .hours to match your 1025 implementation.

# Your classes:

class Flight:
    def __init__(self, hours, flight_type):
        self.hours = float(hours)
        self.flight_type = flight_type

# initial attempt:                              Comments: 
# class Logbook:
#     def __init__(self):
#         self.flight = Flight()                This would error out since we need the arguements hours and flight_type. 
#         self.flights = []                     Logbook starts empty, we are simply storing Flight objects. 
#     def add_flight(self, flight):
#         self.flight = flight                  My list belongs to the logbook so all we need to do to access it is self.flights
#         flights.append(flight)                all we need to do here is self.flights.append(flight)
#     def total_hours(self, flight.hours):      parameter cannot contain a dot, the method already has access to the flights through self
#         self.flight.hours = flight.hours      flight.hours is a single number, we need instead to loop over the list of Flight objects
#         for n in flight.hours:
#             n.sum()
class Logbook:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def total_hours(self):
        total = 0

        for flight in self.flights:
            total += flight.hours

        return total



