import logging
"""
DEBUG -
INFO -
WARNING -
ERROR -
CRITICAL -
"""
logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def add_function(x, y):
    """ Add function """
    return x + y

x = 10
y = 2

add_result = add_function(x, y)
logging.debug(f'Add: {x} + {y} = {add_result}')


