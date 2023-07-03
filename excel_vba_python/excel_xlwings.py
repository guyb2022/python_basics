import xlwings as xw
import pandas as pd

"""
create data and open an excel sheet with the data populated
"""
wk = xw.books.open('example.xlsx')
sheet = wk.sheets('Worksheet')
rg = sheet.range("A1:f6")
print(rg.value)

df = sheet.range("A1:F6").options(pd.DataFrame).value
print(df)

xw.view(df)
wk.close