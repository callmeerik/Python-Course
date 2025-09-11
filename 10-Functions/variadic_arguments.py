"""
            VARIADIC POSITIONAL ARGUMNENTS
        *name_argument
"""
pizzas = {
"Margherita": 8.5,
"Pepperoni": 10.0,
"Veggie": 8.0
}


# ✅ Function with *args for multiple pizza types
def order_multiple_pizzas(customer_name, *pizza_types):
    total = 0
    print(f"{customer_name} ordered:")
    for p in pizza_types:
        price = pizzas.get(p, 0)
        print(f"- {p}: ${price}")
        total += price
    print(f"Total: ${total}")


order_multiple_pizzas("Alice", "Margherita", "Pepperoni")
order_multiple_pizzas("Bob", "Veggie", "Pepperoni", "Margherita")