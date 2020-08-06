# -*- coding: utf-8 -*-
"""Day 5 (Multiple Datasets).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NXfETiUl-A1cxfTwNIm3iunQL5ctPvU5
"""



import pandas as pd

unemp_county = pd.read_csv("output.csv")
unemp_county.head()

df = pd.read_csv("minwage.csv")

act_min_wage = pd.DataFrame()

for name, group in df.groupby("State"):
    if act_min_wage.empty:
        act_min_wage = group.set_index("Year")[["Low.2018"]].rename(columns={"Low.2018":name})
    else:
        act_min_wage = act_min_wage.join(group.set_index("Year")[["Low.2018"]].rename(columns={"Low.2018":name}))

act_min_wage.head()

import numpy as np

act_min_wage = act_min_wage.replace(0, np.NaN).dropna(axis=1)
act_min_wage.head()

def get_min_wage(year, state):
    try:
        return act_min_wage.loc[year][state]
    except:
        return np.NaN

get_min_wage(2012, "Colorado")

# Commented out IPython magic to ensure Python compatibility.
# %%time
# # time will give us the total time to perform some cell's operation.
# 
# unemp_county['min_wage'] = list(map(get_min_wage, unemp_county['Year'], unemp_county['State']))

unemp_county.head()

unemp_county.tail()

unemp_county[['Rate','min_wage']].corr()

unemp_county[['Rate','min_wage']].cov()

pres16 = pd.read_csv("pres16.csv")
pres16.head(15)

top_candidates = pres16.head(10)['cand'].values
print(top_candidates)

#county_2015 = unemp_county[ (unemp_county['Year']==2015 and unemp_county["Month"]=="February") ]



county_2015 = unemp_county[ (unemp_county['Year']==2015) & (unemp_county["Month"]=="February")]

county_2015.head()

state_abbv = pd.read_csv("state_abbv.csv", index_col=0)
state_abbv.head()

state_abbv_dict = state_abbv.to_dict()['Postal Code']

county_2015['State'] = county_2015['State'].map(state_abbv_dict)

county_2015.tail()

print(len(county_2015))
print(len(pres16))

pres16.rename(columns={"county": "County", "st": "State"}, inplace=True)
pres16.head()

for df in [county_2015, pres16]:
    df.set_index(["County", "State"], inplace=True)

pres16 = pres16[pres16['cand']=="Donald Trump"]
pres16 = pres16[['pct']]
pres16.dropna(inplace=True)
pres16.head(2)

county_2015.head(2)

all_together = county_2015.merge(pres16, on=["County", "State"])
all_together.dropna(inplace=True)
all_together.drop("Year", axis=1, inplace=True)
all_together.head()

all_together.corr()

all_together.cov()

