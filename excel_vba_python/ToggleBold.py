import xlwings as xw

def main():
    wb = xw.Book.caller()
    sheet = wb.sheets('Sheet1')
    if sheet['A6'].font.bold:
        sheet['A6'].font.bold = False
    else:
        sheet['A6'].font.bold = True
