import os
import pandas as pd

os.chdir(r"C:\Users\DELL\Desktop\collage\nptel\week_3")

data_csv=pd.read_table("Iris_data_sample.txt",index_col=0,sep=" ")
samp=data_csv.copy(deep=True)
print(data_csv)