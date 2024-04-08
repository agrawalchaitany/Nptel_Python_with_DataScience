import os
import pandas as pd
import numpy as np
os.chdir(r"C:\Users\DELL\Desktop\collage\nptel\week_3")
cars_data=pd.read_csv("Toyota.csv",index_col=0)
cars_data1=cars_data.copy(deep=True)
print(cars_data1.dtypes)
dtype_counts = cars_data1.dtypes.value_counts()
print(dtype_counts)
print(cars_data1.select_dtypes(include=None,exclude=[object]))
print(cars_data1.info())
print(np.unique(cars_data1['KM']))
print(np.unique(cars_data1['HP']))
print(np.unique(cars_data1['Automatic']))
print(np.unique(cars_data1['Doors']))