class Flight:
    def __init__(self, code, destination):
        self.code = code
        self.destination = destination
        self.__passengers = [] # private list

    def add_passenger(self, passenger):
        self.__passengers.append(passenger)


    def show_passengers(self):
        print(f"👥 Passengers on flight {self.code} to {self.destination}:")
        for p in self.__passengers:
            print("-", p.name)