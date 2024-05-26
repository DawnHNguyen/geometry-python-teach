import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = './Lop7/Thong ke/Data lop 7.xlsx'

# Load the Excel file
excel_data = pd.ExcelFile(file_path)

# Select the appropriate sheet by its name or index
sheet_name = excel_data.sheet_names[5]

# Read the sheet into a DataFrame without assuming a header
df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)

sheet_name = df.iloc[0, 0]
df = df.drop([0]).reset_index(drop=True)

# Ensure the DataFrame has at least three rows and multiple columns
if df.shape[0] < 3 or df.shape[1] < 2:
    print("The data does not have enough rows or columns.")
else:
    # Extract the years and values for each class
    years = df.iloc[0, 1:].apply(lambda x: int(x))  # Convert years to int
    values_A = df.iloc[1, 1:].apply(lambda x: float(str(x).strip('%')))  # Convert to float
    values_B = df.iloc[2, 1:].apply(lambda x: float(str(x).strip('%')))  # Convert to float

    # Create the line chart
    plt.figure()
    plt.plot(years, values_A, marker='o', label=df.iloc[1, 0])  # Plot for Class A
    plt.plot(years, values_B, marker='o', label=df.iloc[2, 0])  # Plot for Class B
    plt.title(f'Line Chart for {sheet_name}')
    plt.xlabel(df.iloc[0, 0])  # Label for x-axis from first row first column
    plt.ylabel('Percentage (%)')  # Label for y-axis
    plt.legend()
    
    # Set x-axis and y-axis ticks
    plt.xticks(np.arange(min(years), max(years) + 1, 1))  # x-axis with integer steps
    plt.yticks(np.arange(0, max(max(values_A), max(values_B)) + 5, 5))  # y-axis with steps of 5
    
    plt.grid(True)
    plt.show()
