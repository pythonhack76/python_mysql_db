class Persona:
    def __init__(self, nome, cognome, kg):
        self.nome = nome
        self.cognome = cognome
        self.kg = str(kg)


    def peso(self, nome, cognome, kg = 9):
        print("mi chiamo: " + self.nome + "e peso : " + " " + self.kg)
        frase = f"{nome} ha preso il {cognome}"
        print(frase)


persona1 = Persona("pippo","stella",80)
persona1.peso("utente","cognome")