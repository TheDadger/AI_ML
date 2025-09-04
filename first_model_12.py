import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data_frame=pd.read_csv('housePrices.csv')
# print(data_frame)
print(data_frame.describe())

print(data_frame.isnull().sum())

data_frame=data_frame.dropna()
print(data_frame.isnull().sum())

