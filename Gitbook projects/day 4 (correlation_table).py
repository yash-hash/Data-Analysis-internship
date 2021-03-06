# -*- coding: utf-8 -*-
"""Day 3 (Correlation table).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18gmvTrJ8sKkxjZx06TcPecZoyqnws0qH
"""

import pandas as pd
import numpy as np

df.head()

df = pd.read_csv("minwage.csv")
act_min_wage = pd.DataFrame()
for name, group in df.groupby("State"):
  if act_min_wage.empty:
    act_min_wage = group.set_index("Year")[["Low.2018"]].rename(columns={"Low.2018":name})
  else:
    act_min_wage = act_min_wage.join(group.set_index("Year")[["Low.2018"]].rename(columns={"Low.2018":name}))

# column of states with Year as rows (column index set to Year)
# wiht values of column  - Low.2018
act_min_wage.head()
# Dropping the columns with missign values or NaN type values 
min_wage_corr = act_min_wage.replace(0, np.NaN).dropna(axis=1).corr()
min_wage_corr.head()

import matplotlib.pyplot as plt
plt.matshow(min_wage_corr)
plt.show()

## get abbreviated state names:
labels = [c[:2] for c in min_wage_corr.columns] 
fig = plt.figure(figsize = (10,10))
ax = fig.add_subplot(111) #defining axis, so we can modify\
ax.matshow(min_wage_corr, cmap=plt.cm.RdYlBu) # display the matrix
ax.set_xticks(np.arange(len(labels))) #show all the labels
ax.set_yticks(np.arange(len(labels))) # labels on y axis
ax.set_xticklabels(labels) # set abbreviated labels
ax.set_yticklabels(labels) # set abbreviated labels
plt.show()

# Reading an Html file using URL with pandas
import requests
web = requests.get("https://www.infoplease.com/state-abbreviations-and-state-postal-codes")
dfs = pd.read_html(web.text)

dfs = pd.read_html("https://www.infoplease.com/state-abbreviations-and-state-postal-codes")

for df in dfs:
  print(df.head())
# one for states, other for territories

state_abbv = dfs[0]
state_abbv.head()

### Saving the Dataframe ###
state_abbv.to_csv("state_abbv.csv")

# reading the dataframe back again
state_abbv = pd.read_csv("state_abbv.csv")
state_abbv.head()

# indexing duplicates the columns whenever the dataset is loaded, to avoid it----
state_abbv[["State/District", "Postal Code"]].to_csv("state_abbv.csv", index=False)
state_abbv = pd.read_csv("state_abbv.csv", index_col=0)
state_abbv.head()

abbv_dict = state_abbv.to_dict()
abbv_dict
#### Creates a Dcitionary ###

abbv_dict = abbv_dict["Postal Code"]
abbv_dict

# Redoing our Labels
labels = [abbv_dict[c] for c in min_wage_corr.columns] # get abbreviated state names
### Gives an error ###

abbv_dict['Federal (FLSA)'] = "FLSA"
labels = [abbv_dict[c] for c in min_wage_corr.columns]

# Problem in territory
abbv_dict["Guam"] = "GU"
abbv_dict["Puerto Rico"] = "PR"
labels = [abbv_dict[c] for c in min_wage_corr.columns]
### Final abbreviated state names with no errors

### Plotting the graph ###
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
ax.matshow(min_wage_corr, cmap=plt.cm.RdYlGn) # displays the matrix
ax.set_xticks(np.arange(len(labels)))
ax.set_yticks(np.arange(len(labels)))
ax.set_xticklabels(labels)
ax.set_yticklabels(labels)
plt.show()

