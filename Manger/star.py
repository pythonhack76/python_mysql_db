class Persona:
    def __init__(self, nome, cognome, kg):
        self.nome = nome
        self.cognome = cognome
        self.kg = str(kg)


    def peso(self, nome, cognome, kg = 9):
        print("mi chiamo: " + self.nome + "e peso : " + " " + self.kg)
        frase = f"{nome} ha preso il {cognome}"
        print(frase)

    def fisionomia(self,colore_occhi, altezza, carnagione):
        self.colore_occhi = colore_occhi
        self.altezza = str(altezza)
        self.carnagione = carnagione
        
        caratteristiche = f"{nome} ha {colore_occhi}, {altezza} e {carnagione}"
        print(caratteristiche)


persona1 = Persona("pippo","stella",80)
persona1.peso("utente","cognome")
persona1.fisionomia("azzurri",180, "bianca")