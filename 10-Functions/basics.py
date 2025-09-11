"""
        FUNCTIONS
"""

# function without arguments
def order_pizza():
    print('I want a Pepperoni Pizza')

order_pizza()

# function with arguments
def order_pizza2(pizza_type):
    print(f'I want a {pizza_type}')

order_pizza2('🍍 Hawaiian')

# return values in a function
def calculate_pizza_price(pizza_size: str):
    if pizza_size.lower() == 'short':
        return 12.99
    elif pizza_size.lower() == 'medium':
        return 18.99
    elif pizza_size.lower() == 'family':
        return 24.99
    elif pizza_size.lower() == 'giant':
        return 35.99
    else:
        print(f'❌ Your {pizza_size} pizza size does not exist')

price1 = calculate_pizza_price('medium')
price2 = calculate_pizza_price('giant')

print(f'Price 1: {price1}')
print(f'Price 2: {price2}')