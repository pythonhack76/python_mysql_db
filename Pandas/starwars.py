import pandas as pd

df = pd.read_csv('starwars.csv')
#df = pd.read_json('starwars.json')

#print(df[["name", "height"]][0:10])

print(df.iloc[0,2])