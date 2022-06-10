persona = {
    "nome": "Pippo",
    "cognome": "Sensi",
    "eta": 48,
    "interessi": ["basket","calcio"],
    "indirizzo": {
    "cap": 10092,
    "via": "roma" ,
    "citta": "tivoli"
}


}


operazioni = ("aggiungere","modificare", "eliminare","leggere","termina")


def start():
    operazione = input("cosa vuoi fare?")
    if operazione == operazioni[0]:
        x = input("aggiungi chiave:valore seprati da una virgola: ")
        aggiungi(x.split(","))
    elif operazione == operazioni[1]:
        pass
    elif operazione == operazioni[2]:
        pass
    elif operazione ==operazioni[3]:
        pass

def aggiungi(param):
    chiave = param[0]
    valore = param[1]
    persona[chiave] = valore
    print(persona)

while True:
    start() 