import pandas as pd
import seaborn as sns
import os
import matplotlib.pyplot as plt

# Change directory to where your file is located
os.chdir(r"C:\Users\DELL\Desktop\collage\nptel\week_3")

# Read the CSV file into a DataFrame
churn = pd.read_csv("churn.csv", index_col=0)

missing=churn['TotalCharges'].isnull().sum()








