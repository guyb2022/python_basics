import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlwings as xw
from xlwings import constants as xl_const

def init_excel_sheet(sheet):
    """ Init the excel reader object """
    wk = xw.books.open('test.xlsx')
    wb = xw.Book.caller()
    return wb.sheets(sheet)

def read_df(sheet):
    """ Get the df from excel file"""
    df = sheet.range("A1").options(pd.DataFrame, index=False, expand='table').value
    return df

def aggregate_df(df):
    """ create the aggregate df pre defined criteria """
    df = df.groupby(['sex', 'smoker']).agg({
        'total_bill': 'mean',
        'tip': 'mean',
        'size': 'mean'
    }).reset_index()

    # Rename the columns
    new_columns = {
        'total_bill': 'Mean Total Bill',
        'tip': 'Mean Tip',
        'size': 'Mean Size'
    }
    df = df.rename(columns=new_columns)
    return df

def write_df_with_style(df, sheet):
    """ Write the aggregated df to excel Add style as well """
    headers = ['j1','K1','L1','M1','N1']
    sheet["I1"].value = df
    for header in headers:
        sheet[header].font.bold = True
        sheet[header].api.HorizontalAlignment = xl_const.HAlign.xlHAlignCenter
        sheet[header].api.VerticalAlignment = xl_const.VAlign.xlVAlignCenter

    range_with_borders = sheet.range("I1:N5")
    # Access the underlying Excel Range object using the .api property
    excel_range = range_with_borders.api

    # Apply table borders using Excel's API
    excel_range.Borders(7).LineStyle = 1
    excel_range.Borders(7).Weight = 2
    excel_range.Borders(8).LineStyle = 1
    excel_range.Borders(8).Weight = 2
    excel_range.Borders(9).LineStyle =1
    excel_range.Borders(9).Weight = 2
    excel_range.Borders(10).LineStyle = 1
    excel_range.Borders(10).Weight = 2

def insert_picture_to_excel(sht, cell, fig, pic_name):
    """ Insert the chart into the worksheet"""
    for picture in sht.pictures:
        if picture.name == pic_name:
            picture.delete()
    sht.pictures.add(
        fig,
        name=pic_name,
        update=True,
        left=sht.range(cell).left,
        top=sht.range(cell).top,
        height=250,
        width=400,
    )
    return None

def bar_chart(df, cell, sheet):
        """
        Plot a Bar Graph for selected columns.
        place: position of the chart
        """
        fig, ax = plt.subplots()

        x = np.arange(len(df))  # X-axis values
        y1 = df['Mean Total Bill']  # Values for the first bar chart
        y2 = df['Mean Tip']  # Values for the second bar chart
        y3 = df['Mean Size']  # Values for the third bar chart

        ax.bar(x - 0.2, y1, width=0.2, color='red', align='center')
        ax.bar(x, y2, width=0.2, color='green', align='center')
        ax.bar(x + 0.2, y3, width=0.2, color='blue', align='center')

        ax.set_xticks(x)
        ax.set_xticklabels(['0', '1', '2', '3'])
        ax.set_xlabel('Categories')
        ax.set_ylabel('Values')
        ax.set_title('Bar Chart Example')

        ax.legend(['Mean Total Bill', 'Mean Tip', 'Mean Size'])
        plt.title(f" Mean Total Bill, Mean Tip, Mean Size \n groupby sex and smoker and aggregated with mean\n")
        insert_picture_to_excel(sht=sheet, cell=cell, fig=fig, pic_name="Agrregation and group by example")

@xw.sub
def main():
    # Init the excel sheet
    sheet = init_excel_sheet('Sheet1')

    # Get initial df
    excel_df = read_df(sheet)

    # Run the aggregated function
    df_grouped_agg = aggregate_df(excel_df)

    # Write deata to excel
    write_df_with_style(df_grouped_agg, sheet)

    # Plot the chart
    bar_chart(df_grouped_agg, "I9", sheet)

if __name__ == '__main__':
    xw.Book("test.xlsm").set_mock_caller()
    main()