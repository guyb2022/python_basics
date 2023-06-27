from functools import wraps

def wrapper(func):
    @wraps(func)
    def inner(list_of_vlaues):
        """ This is the inner() method to handle the string manipulation"""
        return [func(value) for value in list_of_vlaues]
    return inner

@wrapper
def camel_case(s):
    """ Turn strings into camel case"""
    return ''.join([word.capitalize()  for word in s.split('_')])

print(camel_case(['great_work_ahead']))


names = [
    'mr_easy_beasy',
    'long_but_short',
    'great_work_ahead'
]




# print(camel_case([s1,s2,s3]))
# print(camel_case.__doc__)


def check_division(func):

    def inner(a, b):
        """ inner function to check division validity"""
        if b == 0:
            print("Cant divide by 0")
            return
        return func(a, b)

    return inner


@check_division
def divide(x, y):
    return x / y

# divide = check_division(divide)

divide(10,0)