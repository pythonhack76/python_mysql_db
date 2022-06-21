import pandas as pd


df = pd.read_csv('starwars.csv')

# df[["Segno","Opposto","Quadro"]] = ["leone","bianco","magico"]
# print(df[["Segno", "Opposto", "Quadro"]])

df.loc[:, "Wii"] = "jkjkjk"
print(df)