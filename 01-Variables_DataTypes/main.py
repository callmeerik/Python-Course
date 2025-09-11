"""
        DATA TYPES  
    - Numerical:
        - Integers
        - Floats
    - Characters
        - Strings
    - Booleans
        - True
        - False
"""

#pizza_name = 'Marggaretta'
#units = 2
#price = 23.99
#withOnion = False

# insert data from keyboard
pizza_name = input('Enter your pizza flavor: ')
quantity = int(input('Enter the number ob pizzaas for ordering: '))
price = 29.99

# print information
print('Pizza Order')
print(f'Pizza type: {pizza_name}')
print(f'Quantity: {quantity}')
print(f'Unit price: {price}')
print(f'Total Price: {price * quantity}')
