# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Start coding here! Use as many cells as you like
list = []
for x,y in netflix_df.iterrows():
    if y['release_year'] >= 1990 and y['release_year'] < 2000 and y['type'] == 'Movie':
        list.append(y['duration'])
    else: pass

plt.hist(list, bins = 20)
plt.show()
duration = 100

short_movie_count = 0
for x,y in netflix_df.iterrows():
    if y['duration'] <= 90 and y['release_year'] >= 1990 and y['release_year'] < 2000 and y['type'] == 'Movie' and y['genre'] == 'Action': short_movie_count += 1

print(short_movie_count)
