import os  # for deleting files

# Function to save an order into a file
def save_order(order):
    try:
        with open("orders.txt", "a") as file:   # append mode
            file.write(order + "\n")
        print("✅ Order saved successfully.")
    except Exception as e:
        print("❌ Error saving order:", e)

# Function to read all orders
def read_orders():
    try:
        with open("orders.txt", "r") as file:
            print("📖 Order List:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("❌ Error: orders.txt does not exist yet.")

# Function to delete the file
def delete_orders_file():
    try:
        os.remove("orders.txt")
        print("🗑️ orders.txt deleted successfully.")
    except FileNotFoundError:
        print("❌ Error: orders.txt not found.")
    except Exception as e:
        print("❌ Error deleting file:", e)

# ---------------------------
# Main Menu
# ---------------------------
while True:
    print("\n📋 Pizza Orders Menu")
    print("1. Add order")
    print("2. Read orders")
    print("3. Delete orders file")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        pizza = input("Enter pizza type: ")
        qty = input("Enter quantity: ")
        save_order(f"{pizza} - {qty}")
    elif choice == "2":
        read_orders()
    elif choice == "3":
        delete_orders_file()
    elif choice == "4":
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice, try again.")
