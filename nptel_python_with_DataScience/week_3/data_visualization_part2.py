import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

# Change directory to where your file is located
os.chdir(r"C:\Users\DELL\Desktop\collage\nptel\week_3")

# Read the CSV file into a DataFrame
cars_data = pd.read_csv("Toyota.csv", index_col=0, na_values=["??","????"])
cars_data.dropna(axis=0, inplace=True)
sns.set(style="darkgrid")
#sns.regplot(x=cars_data['Age'],y=cars_data['Price'])
#sns.regplot(x=cars_data['Age'],y=cars_data['Price'],fit_reg=False)
#sns.lmplot(x='Age',y='Price',data=cars_data,fit_reg=False,hue='FuelType',legend=True,palette="Set1")
#sns.displot(cars_data['Age'],kde=False)
#sns.displot(cars_data['Age'],kde=True,bins=5)
#sns.countplot(data=cars_data,x="FuelType")
#sns.countplot(x="FuelType",data=cars_data,hue="Automatic")
#box_plot
sns.pairplot(cars_data,kind="scatter",hue="FuelType")
plt.show()





