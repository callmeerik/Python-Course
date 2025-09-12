
# ✅ What is a module?
# A module is a separate Python file that contains reusable code (functions, classes, variables).
# We can import it into another file to keep our program organized.

import utils  # Importing our custom pizza module

# Pizza menu (dictionary of pizza prices)
menu = {
    "Margherita": 8.5,
    "Pepperoni": 10.0,
    "Veggie": 8.0,
    "BBQ Chicken": 11.0
}

# Example orders
print(utils.order_summary("Alice", "Pepperoni", 2, menu))
print(utils.order_summary("Bob", "Veggie", 3, menu))

# ✅ Importing a specific function
from utils import calculate_order_total

print("Extra check (Charlie):", calculate_order_total("Margherita", 4, menu))
