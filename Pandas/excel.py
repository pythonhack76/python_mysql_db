import pandas as pd
import openpyxl


df = pd.read_csv('starwars.csv')
df2 = df[["name","height","mass"]]
df3 = df[['name','skin_color']]

#df2.to_excel('nuovo_starwars.xlsx', index=False, sheet_name="FoglioNuovo")

with pd.ExcelWriter("nuovi_starwars.xlsx") as writer:
    df2.to_excel(writer, sheet_name="Totali")
    df3.to_excel(writer, sheet_name="Stats")