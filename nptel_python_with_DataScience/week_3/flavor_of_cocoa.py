import pandas as pd

import os

# Change directory to where your file is located
os.chdir(r"C:\Users\DELL\Desktop\collage\nptel\week_3")

# Read the CSV file into a DataFrame
flavors_of_cocoa = pd.read_csv("flavors_of_cocoa.csv", index_col=0)
print(flavors_of_cocoa['Company Location'].mode())
des=flavors_of_cocoa.describe()