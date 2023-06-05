import logging
import time
from datetime import datetime
from functools import wraps

def my_logger(original_func):
    logging.basicConfig(filename=f"{original_func.__name__}.log", level=logging.INFO)

    @wraps(original_func)
    def wrapper(*args, **kwargs):
        logging.info(f"Run with args: {args} with kwargs: {kwargs}")
        return original_func(*args, **kwargs)

    return wrapper

def my_timer(original_func):
    @wraps(original_func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = original_func(*args, **kwargs)
        end = time.time() - start

        logging.info(f"Runtime for {original_func.__name__}: {round(end, 3)} sec, Time: {datetime.now()}")
        return result

    return wrapper

@my_logger
@my_timer
def display_info_and_time(arg1, arg2):
    print(f"I'm Just a function with {arg1} {arg2}")
    time.sleep(1)

display_info_and_time("Hello", "World")