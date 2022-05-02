import matplotlib
import pandas as pd
import numpy as np

df = pd.read_csv('10000 Sales Records.csv')

# print(df.shape)

df['Order Date'] = pd.to_datetime(df['Order Date'])
# print(df.head())
# print (df.dtypes)
# print (df.groupby('Region').mean())