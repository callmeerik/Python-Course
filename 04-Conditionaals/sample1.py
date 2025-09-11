"""
        IF - ELSE - IF
"""

origin = input("Enter the flight origin: ")
destination = input("Enter your destination: ")
class_name = input('Choose a class (economic | premium economic | business): ')

if class_name.lower() == 'economic':
    print(f'Ticket Details')
    print(f'From: {origin}')
    print(f'To: {destination}')
    print(f'Price: {1200 * 1}')
elif class_name.lower() == 'premium economic':
    print(f'Ticket Details')
    print(f'From: {origin}')
    print(f'To: {destination}')
    print(f'Price: {1200 * 2}')
elif class_name.lower() == 'business':
    print(f'Ticket Details')
    print(f'From: {origin}')
    print(f'To: {destination}')
    print(f'Price: {1200 * 3}')
else:
    print('Wrong class!!')