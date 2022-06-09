#operazioni algebriche 
from turtle import pd
import pandas as pd

ds = {
    'Mesi': ['Gennaio','Febbraio','Marzo','Aprile','Maggio','Giugno','Luglio','Agosto','Settembre','Ottobre','Novembre','Dicembre'],
    'Giorni': [31, 28, 31, 30,31, 30, 31, 31, 30,31, 30,31]
}

df = pd.DataFrame(ds)

print(df)

