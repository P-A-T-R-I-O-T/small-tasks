import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
import pandas as pd





df = sns.load_dataset("flights")
# print(df)
df.index = pd.to_datetime(df.year, format= '%Y') # Преобразуем индыксы в формат DateTime Index
df.drop(columns="year", inplace=True) # Удаляем столбец "year" так как он уже преобразован в индексы
# print(df)
df['passengers'] = pd.to_numeric(df['passengers'], errors='coerce')
# df = df.resample('YE').sum()
print(df)


fig, ax = plt.subplots(figsize = (20,40))
sns_heatmap = sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis')
plt.show()