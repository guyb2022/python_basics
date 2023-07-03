import xlwings as xw

def main():
    wb = xw.Book.caller()
    sheet = wb.sheets('Sheet1')
    sheet['A1'].value = "Pyhton programm called From VBA"
    sheet['A2'].value = "Using xlwings with python"
    sheet['A3'].value = "Great Stuff"
    sheet['A6'].value = 'bold'

    sheet['A1'].color = [247,255,0]
    sheet['A2'].color = [0,255,0]
    sheet['A3'].color = [250,155,190]

    sheet['A5'].font.bold = True
    sheet['A5'].font.italic = True

    sheet['A9'].value = "Condittional logic"
    sheet['A10'].value = "For each Cell F[9]-J[9]"
    sheet['A11'].value = "Test pass if score > 100 else fail"