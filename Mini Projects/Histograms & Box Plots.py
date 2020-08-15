# -*- coding: utf-8 -*-
"""Histograms & Box Plots.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MzqsfELBDP9-SdSADKi6QkgINMmxup5v
"""

import pandas as pd
import matplotlib.pyplot as plt
reviews = pd.read_csv("fandango_scores.csv")
cols = ["FILM", "RT_user_norm", "Metacritic_user_nom", "IMDB_norm", "Fandango_Ratingvalue"]
norm_reviews = reviews[cols]
norm_reviews.head()

## computing frequency distribution of user Ratings
fandango_freq = norm_reviews["Fandango_Ratingvalue"].value_counts()
imdb_freq = norm_reviews["IMDB_norm"].value_counts()
fandango_distribution = fandango_freq.sort_index()
imdb_distribution = imdb_freq.sort_index()
print(imdb_distribution)
print(fandango_distribution)

fig, ax = plt.subplots()
ax.hist(norm_reveiws["Fandango_Ratingvalue"],bins=20, range=(0,5))
plt.show()

fig = plt.figure(figsize=(5,20))
ax1 = fig.add_subplot(4,1,1)
ax1.hist(norm_reveiws["Fandango_Ratingvalue"],20,range=(0,5))
ax1.set_title("Distribution of Fandango Ratings")
ax2 = fig.add_subplot(4,1,2)
ax2.hist(norm_reveiws["RT_user_norm"],20, range=(0,5))
ax2.set_title("Distribution of Rotten Tomaotes Ratings")
ax3 = fig.add_subplot(4,1,3)
ax3.hist(norm_reveiws["Metacritic_user_nom"],20,range=(0,5))
ax3.set_title("Distribution of Metaritic Ratings")
ax4 = fig.add_subplot(4,1,4)
ax4.hist(norm_reveiws["IMDB_norm"],20,range=(0,5))
ax4.set_title("Distribution of IMDB Ratings")
ax.set_ylim([0,50])
plt.show()

"""# BAR PLOTS"""

fig ,ax = plt.subplots()
ax.boxplot(norm_reviews["RT_user_norm"])
ax.set_ylim([0,5])
ax.set_xticklabels("Rotten Tomatoes")
plt.show()

##  Multiple boxplots
fig, ax= plt.subplots()
num_cols = ["RT_user_norm", "Metacritic_user_nom", "IMDB_norm", "Fandango_Ratingvalue"]
ax.boxplot(norm_reveiws[num_cols].values)
ax.set_xticklabels(num_cols, rotation=90)
ax.set_ylim([0,5])
plt.show()

