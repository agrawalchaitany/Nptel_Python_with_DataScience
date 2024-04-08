import os
import pandas as pd
import numpy as np
os.chdir(r"C:\Users\DELL\Desktop\collage\nptel\week_3")
cars_data=pd.read_csv("Toyota.csv",index_col=0,na_values=["??","????"])
cars_data2=cars_data.copy(deep=True)
print(pd.crosstab(index=cars_data2['FuelType'],columns='count',dropna=True))
print(pd.crosstab(index=cars_data2['Automatic'],columns=cars_data2['FuelType'],dropna=True))
print(pd.crosstab(index=cars_data2['Automatic'],columns=cars_data2['FuelType'],normalize=True,dropna=True))
print(pd.crosstab(index=cars_data2['Automatic'],columns=cars_data2['FuelType'],dropna=True,normalize=True,margins=True))
print(pd.crosstab(index=cars_data2['Automatic'],columns=cars_data2['FuelType'],dropna=True,normalize='index',margins=True))
print(pd.crosstab(index=cars_data2['Automatic'],columns=cars_data2['FuelType'],dropna=True,normalize='columns',margins=True))
numerical_data=cars_data2.select_dtypes(exclude=[object])
print(numerical_data.shape)
corr_matrix=numerical_data.corr()
print(corr_matrix)

































