
class Passenger:
    def __init__(self, name, passport):
        self.name = name          # public
        self.__passport = passport  # private (encapsulated)

    # Getter (read private attribute)
    def get_passport(self):
        return self.__passport

    # Setter (update private attribute safely)
    def set_passport(self, new_passport):
        if len(new_passport) >= 5:
            self.__passport = new_passport
            print("✅ Passport updated.")
        else:
            print("❌ Invalid passport number.")

    def get_info(self):
        return f"Passenger: {self.name}, Passport: {self.__passport}"
