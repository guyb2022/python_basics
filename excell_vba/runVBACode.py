import xlwings as xw

wk = xw.books.open('example.xlsm')
displayText = wk.macro('module1.DisplayText')
displayText("Called from Python!")

wk.close