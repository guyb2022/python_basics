
# First usage
def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

my_func = outer_function('Hi')
## Output
# Hi

# Execute the function
my_func()

# Second usage
def decorator_function(func):
    def wrapper_functoin(*args, **kwargs):
        print(f"wrapper execute this before: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper_functoin

@decorator_function
def display(arg1, arg2):
    print(f"I'm Just a function with {arg1} {arg2}")
## The @decorator_function is the same as write:
# display = decorator_function(display)
display('parameters','args')
## Output
# wrapper execute this before: display
# wrapper execute this before: display
# I'm Just a function with args parameters

# work with class
class decoretor_class(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f"wrapper execute this before: {self.original_function.__name__}")
        return self.original_function(*args, **kwargs)

@decoretor_class
def deisplay_class(arg1, arg2):
    print(f"I'm Just a function with {arg1} {arg2}")

deisplay_class('class','args')

# add loging capability
from functools import wraps
# this is used for preserving the original behave
# of the wrapper after we chaiin them togather

def my_logger(original_func):
    import logging
    logging.basicConfig(filename=f"{original_func.__name__}.log", level=logging.INFO)

    @wraps(original_func)
    def wrapper(*args, **kwargs):
        logging.info(
            f"Run with args: {args} and kwargs: {kwargs}")
        return original_func(*args, **kwargs)

    return wrapper

def my_timer(original_func):
    import time

    @wraps(original_func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = original_func(*args, **kwargs)
        end = time.time() - start
        print(f"{original_func.__name__} run in: {end} sec")

    return wrapper

@my_logger
@my_timer
def display_info_multi(arg1, arg2):
    print(f"I'm Just a function with {arg1} {arg2}")

display_info_multi('log', 'time')

