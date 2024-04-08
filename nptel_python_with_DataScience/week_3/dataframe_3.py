import os
import pandas as pd
import numpy as np
os.chdir(r"C:\Users\DELL\Desktop\collage\nptel\week_3")
cars_data=pd.read_csv("Toyota.csv",index_col=0,na_values=["??","????"])
cars_data1=cars_data.copy(deep=True)
print(cars_data1.info())
print(cars_data1.dtypes)