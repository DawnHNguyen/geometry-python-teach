import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = './Lop8/Thong ke/Data lop 8.xlsx'

# Load the Excel file
excel_data = pd.ExcelFile(file_path)

# Select the appropriate sheet by its name or index
sheet_name = excel_data.sheet_names[4]

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
    values = df.iloc[1, 1:].apply(lambda x: float(str(x).replace(',', '.')))  # Convert to float, handling comma decimal

    # Create the line chart
    plt.figure()
    plt.plot(labels, values, marker='o')
    plt.title(f'Line Chart for {sheet_name}')
    plt.xlabel(df.iloc[0, 0])  # Label for x-axis from first row first column
    plt.ylabel(df.iloc[1, 0])  # Label for y-axis from second row first column
     # Set x-axis and y-axis ticks
    plt.xticks(np.arange(min(labels), max(labels) + 1, 1.0))  # x-axis with integer steps
    plt.yticks(np.arange(0, max(values) + 0.25, 0.25))  # y-axis with steps of 0.25
    plt.grid(True)
    plt.show()
