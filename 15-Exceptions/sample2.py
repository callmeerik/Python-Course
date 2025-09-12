# Airline booking with error handling

flights = {
    "AA101": 50,   # available seats
    "BA202": 0,    # fully booked
    "CC303": 25
}

try:
    code = input("Enter flight code (AA101, BA202, CC303): ")
    seats = int(input("Enter number of seats: "))

    if seats <= flights[code]:
        print(f"✅ Booking successful! {seats} seats reserved on {code}.")
    else:
        print("❌ Not enough seats available!")

except KeyError:
    print("Error: Flight code does not exist.")
except ValueError:
    print("Error: Seats must be a number.")
