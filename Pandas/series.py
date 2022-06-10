import pandas as pd

ds = [5,10,15,20,25]

serie = pd.Series(ds, index=["perUno","perDue","perTre","perQuattro","perCinque"])

print(serie)