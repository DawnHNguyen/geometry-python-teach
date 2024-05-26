import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = './Lop8/Thong ke/Data lop 8.xlsx'

# Load the Excel file
excel_data = pd.ExcelFile(file_path)

# Select the appropriate sheet by its name or index
sheet_name = excel_data.sheet_names[5]

# Read the sheet into a DataFrame without assuming a header
df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)

# Use the first cell content as the title and remove the first row
sheet_title = df.iloc[0, 0]
df = df.drop([0]).reset_index(drop=True)

# Ensure the DataFrame has at least two rows and multiple columns
if df.shape[0] < 2 or df.shape[1] < 2:
    print("The data does not have enough rows or columns.")
else:
    # Extract labels and values for each class
    categories = df.iloc[0, 1:]  # Skip the first column which is just a label
    values_A = df.iloc[1, 1:].apply(lambda x: float(str(x).replace(',', '.')))  # Convert to float, handling comma decimal
    values_B = df.iloc[2, 1:].apply(lambda x: float(str(x).replace(',', '.')))  # Convert to float, handling comma decimal

    # Create the bar chart
    x = np.arange(len(categories))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots(figsize=(12, 8))
    rects1 = ax.bar(x - width/2, values_A, width, label=df.iloc[1, 0])
    rects2 = ax.bar(x + width/2, values_B, width, label=df.iloc[2, 0])

    # Add some text for labels, title, and custom x-axis tick labels, etc.
    ax.set_xlabel(df.iloc[0, 0])
    ax.set_ylabel('Số lượng học sinh')
    ax.set_title(f'Column Chart for {sheet_title}')
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.legend()

    # Function to add labels on the bars
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)

    fig.tight_layout()

    plt.show()
