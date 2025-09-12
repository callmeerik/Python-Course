
# Base class
class Staff:
    def __init__(self, name):
        self.name = name

    def role(self):
        return "General Staff"

# Inheritance + Polymorphism
class Pilot(Staff):
    def role(self):
        return f"👨‍✈️ Pilot {self.name} flying the plane"

class FlightAttendant(Staff):
    def role(self):
        return f"🧑‍💼 Attendant {self.name} assisting passengers"
