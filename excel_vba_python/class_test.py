import xlwings as xw
import numpy as np
import pandas as pd

class MyUDFs:
    def __init__(self):
        self.caller = None

    @xw.func
    @xw.arg('name', doc='Name as Input')
    def hello(self, name):
        return f"Hello, {name}!"

# xlwings wrapper functions
@xw.func
@xw.arg('name', doc='Name as Input')
def set_name(name):
    MyUDFs.hello(name)

# calling for class with outer function
@xw.func
@xw.arg('x', np.array, ndim=2, doc='x input')
def double_matrix(x):
    wb = xw.Book.caller()
    MyUDFs.caller = wb
    return 2 * x


my_udfs = MyUDFs()
# register a class function
hello = my_udfs.hello

