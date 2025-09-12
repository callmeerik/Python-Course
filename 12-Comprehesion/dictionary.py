"""
        DICTIONARY COMPREHESION
"""

# ✅ Create a list of pizza names
pizzas = ["Margherita", "Pepperoni", "Veggie", "BBQ Chicken"]

# ✅ Dictionary comprehension: map pizza to its length
pizza_lengths = {p: len(p) for p in pizzas}
print("Pizza lengths:", pizza_lengths)

# ✅ Dictionary comprehension with condition: only pizzas longer than 7 letters
long_pizza_dict = {p: len(p) for p in pizzas if len(p) > 7}
print("Long pizza dict:", long_pizza_dict)

# ✅ Dictionary comprehension with transformation: pizza and uppercase name
uppercase_pizzas = {p: p.upper() for p in pizzas}
print("Uppercase pizza dict:", uppercase_pizzas)
