import matplotlib.pyplot as plt
import pandas as pd
import os

# Change directory to where your file is located
os.chdir(r"C:\Users\DELL\Desktop\collage\nptel\week_3")

# Read the CSV file into a DataFrame
cars_data = pd.read_csv("Toyota.csv", index_col=0, na_values=["??","????"])
cars_data.dropna(axis=0, inplace=True)

# Create a scatter plot
plt.scatter(cars_data['Age'], cars_data['Price'], color='red')

# Set the labels and title
plt.xlabel('Age (Months)')
plt.ylabel('Price (Euros)')
plt.title("Scatter Plot of Car Age vs Price")

# Display the plot
plt.show()
#also do histogram and bars charts