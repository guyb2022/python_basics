import xlwings as xw
import time
from random import randint
import datetime as datetime
import concurrent.futures
from xlwings import constants as xl_const

def get_test_value(value):
    """ Simulate random running time with random result """
    time.sleep(randint(1,3))
    test_score = randint(50,150)
    if test_score > 100:
        color = [3, 192, 60]
    else:
        color = [255, 36, 0]
    return test_score, color, value

@xw.sub
def main():
    """ Main function to perform all releavent function on excell cells"""
    wb = xw.Book.caller()
    sheet = wb.sheets('Sheet1')

    headers = ['F9','G9','H9','I9','J9']
    cells = ['F10','G10','H10','I10','J10']

    for i, header in enumerate(headers):
        sheet[header].value = f"Test {i+1}"
        sheet[header].font.bold = True
        # Set the alignment to center
        sheet[header].api.HorizontalAlignment = xl_const.HAlign.xlHAlignCenter
        sheet[header].api.VerticalAlignment = xl_const.VAlign.xlVAlignCenter

    # The jobs will be executed in threads togather.
    # The time of execution will be as the longets job.
    # Once the last job will finish, all jobs will return.
    with concurrent.futures.ThreadPoolExecutor() as executer:
        futures = [executer.submit(get_test_value, _) for _ in range(5)]

        for future, cell in zip(futures, cells):
            result = future.result()
            sheet[cell].value = result[0]
            sheet[cell].color = result[1]

    print("Done Executing All Jobs in default config")


