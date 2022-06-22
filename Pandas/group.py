import pandas as pd

df = pd.read_csv('starwars.csv')

types = df.groupby(['gender','species'])

#print(types.groups)

for name,group in types:
    print(name)
    print(group)