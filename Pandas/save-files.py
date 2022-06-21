from turtle import pd
import pandas as pd
import os
import pathlib 


df = pd.read_csv('starwars.csv')
df2 = df[["name", "height", "mass"]]


df2.to_csv("file_new.csv")
compressed_df2 = dict(method='zip', archive_name='nuovi_files.csv')
df2.to_csv('nuovi_files.zip', index=False, compression=compressed_df2)

# percorso = pathlib.Path.cwd() 

# print(percorso)