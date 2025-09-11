"""
            Lists
    - Ordered collection of items
    - It's mutable
    - Can store strings, numbers, booleans, or other lists or collections
"""

#=========================================
#       How to create lists?
#=========================================

# empty list
my_list = []

# list with values
passengers = ['Bob', 'Laetitia', 'Stefan', 'Georgia', 'Ron', 'Joshua']


#=========================================
#       Acces to items
#=========================================
print(f'First element: {passengers[0]}')
print(f'All passengers: {passengers}')


#=========================================
#       ♻ Modify Items
#=========================================
passengers[2] = 'Tessa'
print('Modified list: ', passengers)


#=========================================
#       ➕ Add Items
#=========================================
passengers.append('Danubio')
passengers.insert(1, 'Eva')
print('Added items: ', passengers)


#=========================================
#       ❌Remove Items
#=========================================
passengers.remove('Eva')    # remove by value
passengers.pop()            # remove last item
passengers.pop(4)           # remove by index
print('Removed items: ', passengers)


#=========================================
#       ✅ Check if a item exists
#=========================================

if 'Laetitia' in passengers:
    print('The passsenger is onboard')
else:
    print('The passenger is not onboard')

#=========================================
#                Slicing
#=========================================
print(passengers[0:3])      # from 0 to up 3 (not included)
print(passengers[1:])       # from index 1 to end
print(passengers[:4])       # from index 0 to 4 (not included)


#=========================================
#       Loop through lists
#=========================================
for index, passenger in enumerate( passengers, start=1 ):
    print(f'Passenger P00{index}: {passenger}')