# map()
# apply a function to each value of a list

fruits = ['apple', 'watermelon', 'orange']
caps = list( map( lambda f: f.title(), fruits ) )
print(caps)


# filter
# keeps the elemnts where the function return True
nums = [1, 2, 4, 5, 12, 15, 18, 17]
even_nums = list( filter( lambda x: x%2 == 0, nums ) )
print(f"Even  Numbers: {even_nums}")


# reduce
# reduces a sequance to a single value, applying a function
from functools import reduce
nums = [2, 4, 7, 8, 10]
total_sum = reduce( lambda x, y: x + y, nums )
print(f"Total sum of {nums}: {total_sum}")



# zip()
# cmbines multiple iterables element by element

passenger = ['Varonica', 'Erik', 'Andreas', 'wendy']
seats = ['21A', '34J', '1E', '45H']

paired = list( zip( passenger, seats ) )
print(paired)