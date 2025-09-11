
def order_pizza(customer_name, pizza_type="Margherita", quantity=1):
    total_price = quantity * pizzas.get(pizza_type, 0)
    print(f"{customer_name} ordered {quantity} {pizza_type} pizza(s). Total: ${total_price}")

# Example dictionary of pizza prices
pizzas = {
    "Margherita": 8.5,
    "Pepperoni": 10.0,
    "Veggie": 8.0
}

order_pizza("Alice")  # Uses Margherita and quantity 1

order_pizza("Bob", "Pepperoni")  # Quantity defaults to 1


order_pizza("Charlie", "Veggie", 3)


def add_toppings(topping="Cheese", quantity=1):
    print(f"Adding {quantity} portion(s) of {topping}")

add_toppings()             # Uses default Cheese and quantity 1
add_toppings("Olives")    # Quantity 1 by default
add_toppings("Bacon", 2) # Custom topping and quantity
