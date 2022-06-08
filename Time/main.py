import datetime
##############################
# gestione del tempo usando
# giorno, settimana, anno
# minuti e secondi           #
##############################

tempo = datetime.datetime.now()


#%d / %m / %Y
print(tempo.strftime("%d/%m/%Y"))
print(tempo)