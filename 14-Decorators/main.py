#  Decorators in Python
# A decorator is a function that modifies another function.
# Useful for logging, security, timing, etc.

def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished function: {func.__name__}")
        return result
    return wrapper

# ✅ Example: shopping functions

@log_function
def add_to_cart(item):
    print(f"{item} added to cart.")

@log_function
def checkout(total):
    print(f"Checking out with total: ${total}")

# Using decorated functions
add_to_cart("Laptop")
checkout(1200)
