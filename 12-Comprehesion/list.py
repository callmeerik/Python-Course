"""
        list comprehsesion
"""
# ✅ Create a list of pizza names
pizzas = ["Margherita", "Pepperoni", "Veggie", "BBQ Chicken"]

# ✅ List comprehension: all pizza names in uppercase
uppercase_pizzas = [p.upper() for p in pizzas]
print("Uppercase pizzas:", uppercase_pizzas)

# ✅ List comprehension with condition: only pizzas with more than 7 letters
long_pizzas = [p for p in pizzas if len(p) > 7]
print("Long pizzas:", long_pizzas)

# ✅ List comprehension with transformation: lengths of pizza names
pizza_name_lengths = [len(p) for p in pizzas]
print("Pizza name lengths:", pizza_name_lengths)

# pizza prices
prices = [12.99, 21.99, 34.99, 43.99]
price_greather_20 = [ p for p in prices if p > 20 ]
print(price_greather_20)