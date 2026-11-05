# Today:
## Core session

1. **20 min · first attempt:** rebuild Flight(hours, flight_type) and Logbook() with add_flight and total_hours; save before opening notes or AI.
2. **15 min · targeted reading:** compare your October 26 first attempt and repair. Explain self.flights, the loop variable and return.
3. **60 min · build/check:** rebuild with hours_by_type using ordinary loops. Use flights (1.5, training), (2.0, cross_country), (0.75, training): total 4.25; grouped totals 2.25 and 2.0. A second logbook stays empty. Use .hours consistently with your latest code.
4. **35 min · changed practice:** vary flight types/hours; check grouped totals and an empty book. Explain a list of objects versus one Flight; trace each loop variable and the running total.
5. **35 min · files/debug:** Turn the pi search into a function taking text and a query. Explain why substring search differs from membership in readlines(), and why with closes a file but does not create a Python variable scope. Test found/not-found and an empty query; correct those two notes.
6. **15 min · log:** save first attempt/repair, actual time, help, one bug/cause and tomorrow's action.


# Python Data Model, 20 minute reading

The python data model is a description of Python ads a framework
- It formalizes the interfaces of the building blocks of the language itself, e.g. sequences, iterators, functions, classes, context managers, and so on. 

The Python interpreter invokes special methods to perform basic object operations- often triggered by special syntax
- special method names are triggered by leading and trailing double underscores (dunder)

For example the syntax `obj[key]` is supported by the `__getitem__`  special method. 
When we run `my_collection[key]`, the interpreter calls `my_collection.__getitem__(key)`

magic method = special method
dunder = double under
special methods are also known as dunder methods

