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
    jobs = ['F11', 'G11', 'H11', 'I11', 'J11']

    for i, header in enumerate(headers):
        sheet[header].value = f"Test {i+1}"
        sheet[header].font.bold = True
        # Set the alignment to center
        sheet[header].api.HorizontalAlignment = xl_const.HAlign.xlHAlignCenter
        sheet[header].api.VerticalAlignment = xl_const.VAlign.xlVAlignCenter

    # This configuration will print jobs as they are finished
    with concurrent.futures.ThreadPoolExecutor() as executer:
        results = [executer.submit(get_test_value, job) for job in jobs]

        # as_complete print the threads in hte order they are done
        for f in concurrent.futures.as_completed(results):
            sheet[f.result()[2]].value, sheet[f.result()[2]].color = f.result()[0], f.result()[1]

    print("Done Executing All Jobs in an as_complete config")