# NOVEMBER 5 — RECALL: FLIGHT / LOGBOOK
# Time limit: 20 minutes
# No notes, previous code, or AI assistance during the attempt.
# Use ordinary loops. Leave hours_by_type for today's later session.

# PART 1 — BUILD FROM MEMORY (12 minutes)
#
# Create a Flight class:
# - Flight(hours, flight_type) creates one flight.
# - Each flight stores its own hours and flight_type.
# - Use the attribute name .hours consistently.
#
# Create a Logbook class:
# - Logbook() starts with its own empty list of flights.
# - add_flight(flight) stores the supplied Flight object.
# - total_hours() RETURNS the combined hours of its stored flights.
# - An empty logbook returns 0.
#
# Write both classes below:


class Flight:
    def __init__(self, hours, flight_type):
        self.hours = float(hours)
        self.flight_type = flight_type

class Logbook:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def total_hours(self):
        total = 0
        for flt in self.flights:
            total += flt.hours
        return total

        
# PART 2 — CHECK YOUR BEHAVIOR (5 minutes)
#
# Create two separate logbooks.
#
# Add these three Flight objects to the FIRST logbook:
#   1.5 hours, "training"
#   2.0 hours, "cross_country"
#   0.75 hours, "training"
#
# Print the first logbook's total: expected 4.25.
# Print the second logbook's total: expected 0.
#
# Now add a 1.0-hour flight to ONLY the second logbook.
# Print both totals again: expected 4.25 and 1.0.
#
# Write your checks below:
# cessna_172 = Logbook()
flight_1 = Flight(1.5, "training")
flight_2 = Flight(2.0, "cross_country")
flight_3 = Flight(0.75, "training")
cessna_172 = Logbook()
cessna_172.add_flight(flight_1)
cessna_172.add_flight(flight_2)
cessna_172.add_flight(flight_3)
print(cessna_172.total_hours())
# PART 3 — EXPLAIN FROM MEMORY (3 minutes)
#
# Answer briefly in comments:
# 1. What does self refer to?
# refers to the variables associated to the namespace aka class
# 2. How does one Flight differ from a Logbook's list of flights?
# the Logbook stores Flight objects
# 3. Why should each logbook have its own list?
# to be able to track the flights ascociated with that planes logbook
# 4. In your loop, what does the loop variable refer to?
# not sure, confused on this one
# 5. Why must total_hours RETURN its result instead of only printing it?
# not sure as well
# Your answers:


# STOP AT 20 MINUTES AND SAVE THIS FIRST ATTEMPT.
#
# Record:
# - What I completed independently:
# - Where I got stuck:
# - One result I predicted incorrectly:
#
# Make repairs in a separate copy so this attempt stays unchanged.