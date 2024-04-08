import os
import pandas as pd
import numpy as np
os.chdir(r"C:\Users\DELL\Desktop\collage\nptel\week_3")

cars_data=pd.read_csv("Toyota.csv",index_col=0)
samp=cars_data.copy(deep=True)
print(cars_data.index)
print(cars_data.columns)
print(cars_data.size)
print(cars_data.shape)
print(cars_data.memory_usage())
print(cars_data.ndim)
print(cars_data.head(6))
print(cars_data.tail(5))
print(cars_data.at[5,'FuelType'])
print(cars_data.iat[5,5])
print(cars_data.loc[:,'FuelType'])