# Decorator function
def uppercase_decorator(func):
    def wrapper():
        # Get the result from the original function
        result = func()
        # Modify the result by converting it to uppercase
        modified_result = result.upper()
        # Return the modified result
        return modified_result
    # Return the wrapper function
    return wrapper

# Function to be decorated
def greeting():
    return "Hello, world!"

# Decorate the function using the decorator function
greeting = uppercase_decorator(greeting)

# Call the decorated function
print(greeting())  # Output: HELLO, WORLD!