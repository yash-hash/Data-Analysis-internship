# -*- coding: utf-8 -*-
"""Line Plot Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N6VCphNKNLkj0Jy44rc47ixVAzDiDT9F
"""

import pandas as pd
df = pd.read_csv("unrate.csv",parse_dates=["DATE"],index_col=["DATE"])
df.head()

df.dtypes
df.info()

# checking value of an index column
df.index

x = df.iloc[0:12].index.values
y = df['VALUE'].iloc[0:12]
plt.plot(x,y,marker="*",markeredgecolor="blue",color="red")
plt.xticks(x,rotation=90)
plt.xlabel("Month")
plt.ylabel("Unemployment Rate")
plt.title("Monthly Unemployment Trends, 1948")
plt.show()

