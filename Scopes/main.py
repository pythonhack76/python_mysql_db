import datetime

valore = 1976
nomi =['pippo','test1','asus','ibm']
elenco = {
    "nome": 'aldo',
    "cognome": 'pippen',
    "anni": 38
},
{
    "nome": 'grazia',
    "cognome": 'valle',
    "anni": 45
},
{
    "nome": 'enzo',
    "cognome": 'craxi',
    "anni": 56
}

def contaElenco():
    voci = len(elenco)
    print("abbimao " + voci + "voci")



def funzione_test():
    nome = 'pippo'
    print(nome)

def ciclo_valori():
    for nome in nomi:
        print(nome)

def ciclo_dict():
    for nome in elenco:
        print(nome)


tempo = datetime.datetime(2022, 3, 21)

print(tempo)

funzione_test() 
ciclo_valori() 
ciclo_dict() 
contaElenco()