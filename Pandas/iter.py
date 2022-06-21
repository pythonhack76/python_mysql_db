import pandas as pd

#iterare con key:value, iterrows index:row , itertuples

df = pd.read_csv('starwars.csv').head(1)

for index, row in df.iterrows():
    print(row)