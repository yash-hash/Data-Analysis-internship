# -*- coding: utf-8 -*-
"""Day2(Avocado_prices-part 2).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1t2VMuivQAGwAnodcfYPnCM4xMoOY54oN
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("avocado.csv")
df["Date"] = pd.to_datetime(df["Date"]) # converting date column to datetime objects
albany_df = df[df["region"]=="Albany"]
albany_df.set_index("Date", inplace=True)
albany_df["AveragePrice"].plot()

albany_df["AveragePrice"].rolling(25).mean().plot()

albany_df.sort_index(inplace=True)

albany_df["AveragePrice"].rolling(25).mean().plot()

#saving our smoothed data in a new column in data frame
albany_df["price25ma"] = albany_df["AveragePrice"].rolling(25).mean()

albany_df.head()

albany_df.tail()

#Region Column
df["region"]

#converting it to Array
df['region'].values

# a list could also work
df["region"].values.tolist()
print(set(df["region"].values.tolist()))

#Easy method for the above stuff
df["region"].unique()
#prints every value only once

graph_df = pd.DataFrame()

for region in df['region'].unique()[:16]:
    print(region)
    region_df = df.copy()[df['region']==region]
    region_df.set_index('Date', inplace=True)
    region_df.sort_index(inplace=True)
    region_df[f"{region}_price25ma"] = region_df["AveragePrice"].rolling(25).mean()

    if graph_df.empty:
        graph_df = region_df[[f"{region}_price25ma"]]  # note the double square brackets!
    else:
        graph_df = graph_df.join(region_df[f"{region}_price25ma"])

garph_df

df = pd.read_csv("avocado.csv")
df = df.copy()[df["type"]=="organic"]

df["Date"] = pd.to_datetime(df["Date"])

df.sort_values(by="Date", ascending=True, inplace=True)
df.tail()

graph_df = pd.DataFrame()

for region in df['region'].unique():
    region_df = df.copy()[df['region']==region]
    region_df.set_index('Date', inplace=True)
    region_df.sort_index(inplace=True)
    region_df[f"{region}_price25ma"] = region_df["AveragePrice"].rolling(25).mean()

    if graph_df.empty:
        graph_df = region_df[[f"{region}_price25ma"]]  # note the double square brackets! (so df rather than series)
    else:
        graph_df = graph_df.join(region_df[f"{region}_price25ma"])

graph_df.tail()

graph_df.plot(figsize=(8,5), legend=False)

