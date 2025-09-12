
# Function to calculate the price of an order
def calculate_order_total(pizza, quantity, prices):
    return prices.get(pizza, 0) * quantity

# Function to summarize an order
def order_summary(customer, pizza, quantity, prices):
    total = calculate_order_total(pizza, quantity, prices)
    return f"{customer} ordered {quantity} {pizza}(s). Total: ${total}"
