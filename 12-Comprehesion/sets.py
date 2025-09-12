"""
        SET COMPREHESION
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
