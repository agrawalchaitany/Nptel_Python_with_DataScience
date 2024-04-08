import pandas as pd
import seaborn as sns
import os
import matplotlib.pyplot as plt

# Change directory to where your file is located
os.chdir(r"C:\Users\DELL\Desktop\collage\nptel\week_3")

# Read the CSV file into a DataFrame
mtcars = pd.read_csv("mtcars.csv", index_col=0)
plt.scatter(mtcars['mpg'],mtcars['wt'])
sns.set(style="darkgrid")
sns.regplot(y=mtcars['mpg'],x=mtcars['wt'])
plt.show()







