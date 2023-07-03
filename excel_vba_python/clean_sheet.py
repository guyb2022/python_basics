import xlwings as xw

@xw.sub
def main():
    """ Main function to perform cleaning function"""
    wb = xw.Book.caller()
    sheet = wb.sheets('Sheet1')
    cells = ['A1','A2','A3','A6','A9','A10','A11','F9','G9','H9','I9','J9']
    for cell in cells:
        sheet[cell].value = None
        sheet[cell].color = None

# Entry point of the script
if __name__ == '__main__':
    xw.Book("python_vba.xlsm").set_mock_caller()
    main()