"""
            FUNCTIONAL PROGRAMMING
"""

# First-class functions
# you can pass them like arguments, assign them to variables
# return them from other functions

def square(x):
    return x * x

print(f"2^2 = {square(2)}")

# Higher Order Functions
# a function that takes another functions as arguments
def apply(func, var):
    return func(var)

print( apply( abs, -20 ) )


# Lambdas
# or anonymous functions

mayus = lambda c: c.upper()
print( mayus("python") )

adding = lambda x, y: x + y
print( adding(23, 89) )