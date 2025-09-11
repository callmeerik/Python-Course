"""
        DICTIONARIES
    ✅ oRDERED
    ❌ nOT DUPLICATED
"""

# 📘 Python Dictionaries Tutorial - Pizza Example

# ✅ Creating a dictionary of pizza prices
pizzas = {
    "Margherita": 8.5,
    "Pepperoni": 10.0,
    "Hawaiian": 9.0,
    "Veggie": 8.0
}
print("Pizza menu:", pizzas)

# ✅ Accessing price by pizza name
print("Price of Pepperoni:", pizzas["Pepperoni"])

# ✅ Adding a new pizza
pizzas["BBQ Chicken"] = 11.0
print("After adding BBQ Chicken:", pizzas)

# ✅ Updating the price of a pizza
pizzas["Margherita"] = 9.0
print("After updating Margherita price:", pizzas)

# ✅ Removing a pizza from the menu
del pizzas["Hawaiian"]
print("After removing Hawaiian:", pizzas)

# ✅ Checking if a pizza is on the menu
print("Veggie" in pizzas)   # True
print("Hawaiian" in pizzas) # False

# ✅ Iterating through the menu
for pizza, price in pizzas.items():
    print(f"{pizza}: ${price}")

# ✅ Dictionary with ingredients for each pizza
ingredients = {
    "Margherita": ["Tomato", "Mozzarella", "Basil"],
    "Pepperoni": ["Tomato", "Mozzarella", "Pepperoni"],
    "Veggie": ["Tomato", "Mozzarella", "Peppers", "Onions"]
}

for pizza, items in ingredients.items():
    print(f"Ingredients for {pizza}: {items}")
