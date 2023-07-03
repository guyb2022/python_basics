import openpyxl
import pandas as pd

# Open the Excel file
book = openpyxl.load_workbook("example.xlsx")

# Get the worksheet by name
sheet = book["Worksheet"]

# Now you can work with the sheet
# For example, print the value of cell A1
print(sheet["A1"].value)
# sheet['b15'] = 200
# Print the data
for row in sheet.iter_rows(min_row=1, max_row=6, min_col=2, max_col=4,
                           values_only=True):
    print(row)

# save the file
book.save("example.xlsx")

# working with pandas
df = pd.read_excel('example.xlsx', engine="openpyxl")
# print(df.iloc[:2, 2:5])
print(df[df['Name'].str.match('a')])

print(df.groupby('Class').get_group('a').mean())
