### 1 · Rebuild Flight · 30 minutes

Start in a separate practice file, for example `practice/oop_consolidation_2026_10_22.py`. Keep existing work.

For the first 20 minutes, close the book, earlier code and AI. Write `Flight(date, aircraft, duration, flight_type="training")`, with duration measured consistently in **hours**.

- Store the supplied values as instance attributes.
- Give each instance a default `reviewed=False` attribute.
- Add `duration_minutes()` returning a number and `describe()` returning a useful string.
- Create three flights. Change one flight's duration and reviewed flag; check the other flights retain their own values.
- Explain what class, instance, attribute, method, `self` and `__init__` mean using your code.

Use the last 10 minutes to repair one specific gap. Record whether you used a hint. If most of the class still needs support, spend the next build block repairing this prerequisite.

### 2 · Targeted reading · 20 minutes

Use **Python Crash Course, chapter 9**, only for gaps exposed above: using classes, setting default attribute values and modifying attributes. Read **Instances as Attributes** if you have not reached it; it can support today's composition exercise without completing an inheritance exercise first.

Reference: Python Tutorial §9.1: names and objects and §9.3.5: class and instance variables. The latter includes the shared-list mistake and its repair.

Close each small section and explain it before coding. Save the inheritance, overriding, `super()` and imports assignment for the next session.

### 3 · Build Logbook and independent state · 65 minutes

Use ordinary loops, lists and dictionaries. Keep both classes in the practice file for this session.

Write `Logbook()` with a new empty `self.flights` list created during each instance's initialization. Add:

- `add_flight(flight)`: append the supplied Flight object.
- `total_hours()`: return the sum of the stored flight durations; return zero for an empty logbook.
- `hours_by_type()`: return a dictionary mapping each flight type to its total hours; return an empty dictionary when empty.

Use this fixed dataset before changing any objects:

| Date | Aircraft | Hours | Type |
| --- | --- | --- | --- |
| 2026-10-19 | C172 | 1.50 | training |
| 2026-10-20 | PA28 | 2.00 | cross_country |
| 2026-10-21 | C172 | 0.75 | training |

Expected checks: total **4.25 hours**; training **2.25**; cross_country **2.00**; individual minutes **90, 120, 45**.

Make a second empty logbook; adding to the first must leave the second empty. In a separate tiny broken example, put `flights = []` on the class, reproduce unwanted sharing, then repair it. Explain why creating a list inside each `__init__` fixes that bug.

### 4 · Composition, references and filtering · 55 minutes

Add `flights_by_aircraft(aircraft)`, returning a **new list** of matching Flight objects; no match returns an empty list.

Use these experiments in order. Predict each result before running it.

1. Store a Flight in a Logbook, then change that Flight's duration through its original variable. Recompute the total.
2. Reassign that original variable to a different Flight. Check which Flight the Logbook still contains.
3. Store the same Flight object in two otherwise separate Logbooks. Change that Flight and explain why both totals can change even though the two lists are different.
4. Make a shallow list copy, for example with `list(book.flights)`. Remove an item from the copy, then separately modify one Flight still referenced by both lists. Explain the two different effects.
5. Filter the original dataset for C172 and PA28, then an aircraft with no flights.

Write a three-sentence design note: **a Logbook has Flight objects; each Logbook owns a separate list; adding/filtering shares the existing Flight objects rather than copying their data.** Explain why Logbook does not need to inherit from Flight.

### 5 · Check and debug · 35 minutes

Use small `assert` checks or your existing test setup. Reset to the original dataset where needed.

- Empty totals and grouping return zero and an empty dictionary.
- The three sample flights give the expected total and grouping.
- A different dataset with two flights of the same type still groups correctly.
- Two Logbooks have separate lists.
- Changing one of two distinct Flights leaves the other unchanged.
- Aircraft filtering returns all matches and handles no matches.
- Mutation, rebinding and shallow-copy experiments match your predictions.

Record one real failure, its cause and its repair. If all checks pass initially, reproduce and explain the deliberate class-list bug from block 3.

### 6 · Combine the three math tasks · 45 minutes

**15 minutes · October 19:** for `u=(1,2,3)` and `v=(4,0,-1)`, calculate the dot product, squared Euclidean distance and Euclidean distance by hand. Check with ordinary Python. State the vector dimensions and which outputs are scalars.

**15 minutes · October 20:** let `A=[[1,2,0],[0,1,3]]` and `B=[[1,0],[2,1],[0,2]]`. Calculate AB by hand. Give the input/output shapes, explain whether BA is valid and state its shape; explain why AA is invalid.

**15 minutes · October 21:** state nonnegativity, identity of indiscernibles, symmetry and triangle inequality. Illustrate them with ordinary distance on the number line. Use points 0, 1 and 2 to check whether **squared** distance satisfies triangle inequality. Explain why checking examples differs from a general proof.

### 7 · Independent reconstruction and a new requirement · 40 minutes

Close notes, prior code, documentation and AI for the initial attempt. In a new file:

- Rebuild a smaller Flight and Logbook with `add_flight()` and `total_hours()`.
- Add a new method, `flights_longer_than(min_hours)`, returning flights whose duration is **strictly greater than** the threshold.
- Check empty input, one match, multiple matches and a flight exactly equal to the threshold.
- Explain `self`, separate instance state, the has-a relationship and mutation versus rebinding aloud.

If you stall, save the independent attempt, get one small hint, repair it and record the help. A later changed attempt establishes independence.

### 8 · Save and log · 10 minutes

Save useful work and commit it if working in your preparation repository. Record actual coding/reading minutes, one bug/fix, which tasks needed help and the next smallest step. Today's targets are **225 programming minutes + 20 reading + 45 math + 10 logging = 300 focused minutes**; actual work may differ.

### Completion check

- [ ]  I can build and explain Flight and Logbook.
- [ ]  Totals, grouping, filtering and empty cases work on two datasets.
- [ ]  I can reproduce and repair shared list state.
- [ ]  I can explain mutation, rebinding, shared Flight objects and shallow list copies.
- [ ]  I attempted the changed requirement independently and recorded any help.
- [ ]  I completed the three short math tasks and saved honest evidence.