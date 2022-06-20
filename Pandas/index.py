#operazioni algebriche 
from turtle import pd
import pandas as pd

ds = {
    'Mesi': ['Gennaio','Febbraio','Marzo','Aprile','Maggio','Giugno','Luglio','Agosto','Settembre','Ottobre','Novembre','Dicembre'],
    'Giorni': [31, 28, 31, 30,31, 30, 31, 31, 30,31, 30,31],
    "Stagione": ["Inverno","Inverno","Primavera","Primavera","Primavera","Estate","Estate","Estate","Autunno","Autunno","Autunno","Inverno"],
    "Festivita": ["Capdanno","Carnevale","Festa delle Donne","Pasqua","Festa della Madonna","Spring Break","Rivoluzione Francese","Compleanno","Compleanno","Rivoluzione Russa","Festa Esercito","Natale"]
}

df = pd.DataFrame(ds, index=["Riga1", "Riga2", "Riga3","Riga4","Riga5","Riga6","Riga7","Riga8","Riga9","Riga10","Riga11","Riga12"])

print(df.loc["Riga2"])

