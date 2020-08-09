# -*- coding: utf-8 -*-
"""Day 6 ML with scikit learn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iXFQ4gg0b5l5zjXL3sDlZUSTGqFLzP_c
"""

import pandas as pd

df = pd.read_csv("diamonds.csv", index_col=0)
df.head()

df['cut'].unique()

## Creating a dictionary for categorical variables
cut_class_dict = {"Fair": 1, "Good": 2, "Very Good": 3, "Premium": 4, "Ideal": 5}

df['clarity'].unique() # Columns names are case senstitive

# creating dictionaries for clarity & color column
clarity_dict = {"I3": 1, "I2": 2, "I1": 3, "SI2": 4, "SI1": 5, "VS2": 6, "VS1": 7, "VVS2": 8, "VVS1": 9, "IF": 10, "FL": 11}
color_dict = {"J": 1,"I": 2,"H": 3,"G": 4,"F": 5,"E": 6,"D": 7}

# Mapping it to the dataet
df['cut'] = df['cut'].map(cut_class_dict)
df['clarity'] = df['clarity'].map(clarity_dict)
df['color'] = df['color'].map(color_dict)
df.head()

# with machine learning using linear regression 
## using SGDRegeressor
import sklearn
from sklearn.linear_model import SGDRegressor

df = sklearn.utils.shuffle(df)
# always shuffle your data to avoid any biasesthat may merge b/c of some order.
x = df.drop("price", axis=1).values
y = df["price"].values

test_size = 200
x_train = x[:-test_size]
y_train = y[:-test_size]

x_test = x[-test_size:]
y_test = y[-test_size:]

clf = SGDRegressor(max_iter=1000)
clf.fit(x_train, y_train)
print(clf.score(x_test, y_test))

for x,y in list(zip(x_test, y_test))[:10]:
  print(clf.predict([x])[0],y)

from sklearn import svm

clf = svm.SVR()

clf.fit(x_train, y_train)
print(clf.score(x_test, y_test))

for X,y in list(zip(x_test, y_test))[:10]:
    print(clf.predict([X])[0], y)

clf = SGDRegressor(max_iter=10000)
clf.fit(x_train, y_train)
print(clf.score(x_test, y_test))

for x,y in list(zip(x_test, y_test))[:10]:
  print(clf.predict([x])[0],y)

from sklearn import svm, preprocessing
df = sklearn.utils.shuffle(df)
x = df.drop('price', axis=1).values
x = preprocessing.scale(x)
y = df["price"].values

test_size = 200

X_train = X[:-test_size]
y_train = y[:-test_size]

X_test = X[-test_size:]
y_test = y[-test_size:]

clf = svm.SVR()

clf.fit(x_train, y_train)
print(clf.score(x_test, y_test))

for x,y in list(zip(x_test, y_test))[:10]:
  print(f"model predicts {clf.predict([x])[0]},real value: {y}")
