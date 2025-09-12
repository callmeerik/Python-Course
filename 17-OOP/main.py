from flight import Flight
from passenger import Passenger
from staff import Pilot, FlightAttendant

# Create a flight
flight1 = Flight("AA101", "New York")

# Add passengers
p1 = Passenger("Alice", "P12345")
p2 = Passenger("Bob", "P67890")
flight1.add_passenger(p1)
flight1.add_passenger(p2)

# Show passengers
flight1.show_passengers()

# Test encapsulation
print("\n🔒 Encapsulation Example:")
print(p1.get_info())          # Access via method
p1.set_passport("P11111")     # Update passport safely
print(p1.get_info())

# Staff (Inheritance + Polymorphism)
staff_members = [
    Pilot("Captain Smith"),
    FlightAttendant("Emily")
]

print("\n✈️ Flight Crew Roles:")
for member in staff_members:
    print(member.role())  # Polymorphism in action
