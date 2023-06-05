from functools import wraps

def decorator_function(func):

    @wraps(func)
    def inner(*args, **kwargs):
        """ Handle the args and kwargs printing"""
        print("I'm the wrapper, lets use args and kwargs")
        print(f"args: {[arg for arg in args]}")
        print(f"kwargs: {[{key: value} for key, value in kwargs.items()]}")
        return func(*args, **kwargs)
    return inner

@decorator_function
def display(*args, **kwargs):
    """ Simple function using args & kwargs"""
    print("display output: \n"\
          f"I'm Just a function with \nargs: {args} \nkwargs: {kwargs}")

display('Apple', 'Banana', fruit='Apple', taste='Sweet', color='Red')

# Output
# I'm the wrapper, lets use args and kwargs
# args: ['Apple', 'Banana']
# kwargs: [{'fruit': 'Apple'}, {'tastes': 'Sweet'}, {'color': 'Red'}]
# display output:
# I'm Just a function with
# args: ('Apple', 'Banana')
# kwargs: {'fruit': 'Apple', 'tastes': 'Sweet', 'color': 'Red'}