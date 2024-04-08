import pandas as pd
import seaborn as sns
import os
import matplotlib.pyplot as plt

# Change directory to where your file is located
os.chdir(r"C:\Users\DELL\Desktop\collage\nptel\week_3")

# Read the CSV file into a DataFrame
diamond = pd.read_csv("diamond.csv", index_col=0)

#sns.set(style="darkgrid")
#sns.boxplot(data=diamond , x=diamond['price'],y=diamond['cut'])
plt.boxplot( diamond['price'],diamond['cut'])
plt.show()











