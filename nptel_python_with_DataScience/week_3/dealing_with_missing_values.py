
import pandas as pd

import os

# Change directory to where your file is located
os.chdir(r"C:\Users\DELL\Desktop\collage\nptel\week_3")

# Read the CSV file into a DataFrame
cars_data = pd.read_csv("Toyota.csv", index_col=0, na_values=["??","????"])

cars_data2=cars_data.copy()
cars_data3=cars_data.copy()
print(cars_data2.isna().sum())
missing=cars_data2[cars_data2.isnull().any(axis=1)]
pd.DataFrame(missing)
print(cars_data2.describe())






























