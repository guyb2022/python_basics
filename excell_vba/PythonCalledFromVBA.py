import xlwings as xw

def main():
    wb = xw.Book.caller()
    sheet = wb.sheets('Sheet1')
    sheet['A1'].value = "Pyhton programm called From VBA"
    sheet['A2'].value = "Using xlwings, its Great!!!"
    sheet['A3'].value = "This is Great!!!"