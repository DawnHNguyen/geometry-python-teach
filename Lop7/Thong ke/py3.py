import pandas as pd
import matplotlib.pyplot as plt

file_path = './Lop7/Thong ke/Data lop 7.xlsx'

# Load the Excel file
excel_data = pd.ExcelFile(file_path)

# Select the appropriate sheet by its name or index
sheet_name = excel_data.sheet_names[3]

# Read the sheet into a DataFrame without assuming a header
df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)

sheet_name = df.iloc[0, 0]
df = df.drop([0]).reset_index(drop=True)

# Ensure the DataFrame has at least two rows and multiple columns
if df.shape[0] < 2 or df.shape[1] < 2:
    print("The data does not have enough rows or columns.")
else:
    # Extract labels and values from the first and second rows respectively
    labels = df.iloc[0, 1:]  # Skip the first column which is just a label
    values = df.iloc[1, 1:]

    # Create the pie chart
    plt.figure()
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title(f'Pie Chart for {sheet_name}')
    plt.show()
