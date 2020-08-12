# -*- coding: utf-8 -*-
"""Multiple Plots.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/194vBR7nvGZa3syZYxfnjSBzqf6X8ub7_
"""

import pandas as pd
df = pd.read_csv("unrate.csv", parse_dates=["DATE"])
df.head()

import matplotlib.pyplot as plt
x = df["DATE"].iloc[0:12]
y = df["VALUE"].iloc[0:12]
plt.plot(x,y, marker="*", markeredgecolor="blue", color="red")
plt.xticks(x,rotation=90)
plt.xlabel("Month")
plt.ylabel("unemployment Rate")
plt.title("Unemployment rate trends for month, 1948")
plt.show()

fig = plt.figure(figsize=(12,5))
fig,ax = plt.subplots()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(df["DATE"].iloc[0:12], df["VALUE"].iloc[0:12], marker="o", markeredgecolor="red")
ax2.plot(df["DATE"].iloc[12:24], df['VALUE'].iloc[12:24], marker="o", markeredgecolor="red")
plt.show()

# range function
fig = plt.figure(figsize=(12,5))
for i in range(2):
  ax = fig.add_subplot(2,1,i+1)
  start_index = i*12
  end_index = (i+1)*12
  subset = df[start_index:end_index]
  ax.plot(subset["DATE"], subset['VALUE'], marker="o", markeredgecolor="red")
plt.show()

# five months data
fig = plt.figure(figsize=(12,12))
rows = 5
column = 1
for i in range(0,5):
  ax = fig.add_subplot(5,1,i+1)
  start_index = i*12
  end_index = (i+1)*12
  subset = df[start_index:end_index]
  ax.plot(subset["DATE"], subset['VALUE'], marker="o", markeredgecolor="red")
plt.show()

# Extracting month from DataFrame
df["MONTH"] = df["DATE"].dt.month
print(df['MONTH'])
# RETURNS INTEGER VALUE FOR EACH MONTH
# 1 -JANUARY.....2 - FEBRUARY

# Data for two consecutive months
plt.figure(figsize=(6,6))
plt.plot(df["MONTH"].iloc[12:24], df["VALUE"].iloc[12:24],marker="o")
plt.plot(df["MONTH"].iloc[0:12], df["VALUE"].iloc[0:12], marker="o")
plt.xlabel("Month")
plt.ylabel("Unemployment Trends")
plt.title("Monthly Unemployment trends")
plt.show()

# data for five consecutive Years
plt.figure(figsize=(6,6))
plt.plot(df["MONTH"].iloc[48:60], df["VALUE"].iloc[48:60],marker="o",c="black",label="1952")
plt.plot(df["MONTH"].iloc[36:48], df["VALUE"].iloc[36:48],marker="o",c="orange", label="1951")
plt.plot(df["MONTH"].iloc[24:36], df["VALUE"].iloc[24:36], marker="o",c="green", label="1950")
plt.plot(df["MONTH"].iloc[12:24], df["VALUE"].iloc[12:24],marker="o",c="blue", label="1949")
plt.plot(df["MONTH"].iloc[0:12], df["VALUE"].iloc[0:12], marker="o", c="red", label="1948")
plt.xlabel("Month, Integer")
plt.ylabel("Unemployment Rate, Percent")
plt.title("Monthly Unemployment trends, 1948-1952")
plt.legend(loc="upper left")
plt.show()
