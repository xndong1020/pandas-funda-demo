import numpy as np
import pandas as pd


COLS_TO_USE = ['id', 'artist', 'title', 'medium', 'year', 'acquisitionYear', 'height', 'width', 'units']
df = pd.read_csv('artwork_data.csv', index_col='id', usecols=COLS_TO_USE)

print(df)

df.to_pickle('df.pickle')