import os
import pandas as pd

# Change directory to where your file is located
os.chdir(r"C:\Users\DELL\Desktop\collage\nptel\week_3")

# Read the CSV file into a DataFrame
cars_data = pd.read_csv("Toyota.csv", index_col=0)

# Create a deep copy of the DataFrame
cars_data1 = cars_data.copy(deep=True)

# Insert a new column for Price_Class
cars_data1.insert(10, "Price_Class", "")

# Iterate through each row to assign Price_Class based on Price
for i in range(len(cars_data1)):
    if cars_data1['Price'][i] <= 8450:
        cars_data1.loc[i, 'Price_Class'] = "low"
    elif cars_data1['Price'][i] >= 11950:
        cars_data1.loc[i, 'Price_Class'] = "High"
    else:
        cars_data1.loc[i, 'Price_Class'] = "medium"

# Count the occurrences of each Price_Class
print(cars_data1['Price_Class'].value_counts())
