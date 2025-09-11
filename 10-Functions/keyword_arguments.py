"""
            KEYWORD ARGUMENTS
    **kwargsis a type of argument in Python that allow you
    write arguments with a value.

    **kwargs is like a dictionary
"""

pizzas = {
    "Margherita": 8.5,
    "Pepperoni": 10.0,
    "Veggie": 8.0
}

def order_pizza(customer_name, **pizza_name):
    total_price = 0
    print(f"Order {customer_name}")

    for pizza, quantity in pizza_name.items():
        price = pizzas.get(pizza, 0) * quantity
        print(f"- {pizza} x {quantity} = {price}")
        total_price += price
    print(f"Total price: {total_price}")

order_pizza("Charlie", Margherita=2, Pepperoni=1)
order_pizza("Diana", Veggie=3, Margherita=1, Pepperoni=2)