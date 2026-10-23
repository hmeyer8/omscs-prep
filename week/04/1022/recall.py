# Flight(date, aircraft, duration, flight_type="training")
# duration measured consistently in **hours**.

# - Store the supplied values as instance attributes.
# - Give each instance a default `reviewed=False` attribute.
# - Add `duration_minutes()` returning a number and `describe()` returning a useful string.
# - Create three flights. Change one flight's duration and reviewed flag; check the other flights retain their own values.
# - Explain what class, instance, attribute, method, `self` and `__init__` mean using your code.

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