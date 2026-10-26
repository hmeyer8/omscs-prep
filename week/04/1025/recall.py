# my version of Flight and Logbook: 
# Logbook you add the plane and current hours upon initialiation
# Under logbook we will have a describe method that gives us a full rundown of all logged flights
# Flight will live as an instance attribute
# under Flight you add flights and type hours

class Flight:
    """Represent one flight."""

    def __init__(self, hours, flight_type):
        self.hours = float(hours)
        self.flight_type = flight_type

    def describe(self):
        return f"{self.flight_type}: {self.hours} hours"


class Logbook:
    """Store flights for one aircraft."""

    def __init__(self, aircraft, hours):
        self.aircraft = aircraft
        self.starting_hours = float(hours)
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def total_hours(self):
        """Return hours from the flights logged here."""
        total = 0

        for flight in self.flights:
            total += flight.hours

        return total

    def current_hours(self):
        """Return starting hours plus newly logged hours."""
        return self.starting_hours + self.total_hours()

    def describe(self):
        print(f"Aircraft: {self.aircraft}")
        print(f"Starting hours: {self.starting_hours}")
        print("Logged flights:")

        if not self.flights:
            print("No flights logged yet.")

        for flight in self.flights:
            print(f"  {flight.describe()}")

        print(f"Total logged hours: {self.total_hours()}")
        print(f"Current aircraft hours: {self.current_hours()}")


# Create a logbook for an aircraft starting at 100 hours.
book = Logbook("C172", 100)

# Create individual Flight objects.
flight_1 = Flight(1.5, "training")
flight_2 = Flight(2.0, "cross_country")

# Store those objects in the logbook.
book.add_flight(flight_1)
book.add_flight(flight_2)

book.describe()

# Check that another logbook has independent state.
other_book = Logbook("PA28", 250)
print(f"Other logbook's logged hours: {other_book.total_hours()}")