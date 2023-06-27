import time
import logging
from datetime import datetime

# First usage
def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

my_func = outer_function('Hi')
## Output
# Hi

# # Execute the function
# my_func()

# Second usage
def decorator_function(func):
    def wrapper_functoin(*args, **kwargs):
        print(f"wrapper execute this before: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper_functoin

@decorator_function
def display(arg1, arg2):
    print(f"I'm Just a function with {arg1} {arg2}")
# ## The @decorator_function is the same as write:
# # display = decorator_function(display)
# display('parameters','args')
# ## Output
# # wrapper execute this before: display
# # wrapper execute this before: display
# # I'm Just a function with args parameters

# work with class
class DecoretorClass(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f"wrapper class: {self.original_function.__name__}")
        return self.original_function(*args, **kwargs)

@DecoretorClass
def display_class(*args, **kwargs):
    print(f"I'm Just a function with args: {args} and kwargs: {kwargs} ")

# display_class('These','many','class','args', params='Not relevant')

# add loging capability
from functools import wraps

def my_logger(original_func):
    logging.basicConfig(filename=f"{original_func.__name__}.log", level=logging.INFO)

    @wraps(original_func)
    def wrapper(*args, **kwargs):
        """ Handle the logging"""
        logging.info(
            f"Run with args: {args} with kwargs: {kwargs}")
        return original_func(*args, **kwargs)
    return wrapper

def my_timer(original_func):
    @wraps(original_func)
    def wrapper(*args, **kwargs):
        """ Calaulate the runtime for a called function"""
        start = time.time()
        original_func(*args, **kwargs)
        end = time.time() - start
        formatted_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logging.info(
            f"{original_func.__name__} run in: {round(end,3)} sec, Time: {formatted_datetime}")
        return round(end,3)
    return wrapper

@my_timer
@my_logger
def display_info_and_time(*args, **kwargs):
    print(f"I'm Just a function with args:{args} and kwargs:{kwargs} ")
    time.sleep(1)

display_info_and_time('log', 'time', params='Not relevant')



