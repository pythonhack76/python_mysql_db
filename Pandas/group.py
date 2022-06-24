import pandas as pd

#conteggio, min e max, count, mean count

df = pd.read_csv('starwars.csv')

types = df.groupby(['gender','species'])

#print(types.groups)

for name,group in types:
    print(name)
    print(group)