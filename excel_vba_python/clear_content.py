import xlwings as xw

@xw.sub
def main():
    """ Main function to perform cleaning function"""
    # Get the active sheet
    wb = xw.Book.caller()
    sheet = wb.sheets('Sheet1')
    # sheet = xw.sheets.active
    cells = ['F10','G10','H10','I10','J10', 'F11', 'G11', 'H11', 'I11', 'J11']
    # checkbox = get_checkbox_state(sheet, 'B1')
    # checkbox = sheet.range('B15').api.Value
    # print(checkbox)
    for cell in cells:
        sheet[cell].value = None
        sheet[cell].color = None

# Entry point of the script
if __name__ == '__main__':
    xw.Book("python_vba.xlsm").set_mock_caller()
    main()