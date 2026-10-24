class Flight:
    def __init__(self, date, aircraft, duration, flight_type="training"):
        self.date = date
        self.aircraft = aircraft
        self.duration = float(duration)  # Hours; allows values like 1.5
        self.flight_type = flight_type
        self.reviewed = False

    def duration_minutes(self):
        return self.duration * 60

    def describe(self):
        status = "reviewed" if self.reviewed else "not reviewed"

        return (
            f"{self.date}: {self.aircraft}, "
            f"{self.duration} hours ({self.duration_minutes()} minutes), "
            f"type: {self.flight_type}, {status}."
        )



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