from connect import *

class Persona:
    def __init__(self, nome, cognome, anni = 0):
        self.nome = nome
        self.cognome = cognome
        self.anni = str(anni) 

    def show_persona(self):
        print("ecco il signor " + self.nome + " " + self.cognome + " di anni " + self.anni)
        


persona1 = Persona('Mario','Rossi', 45)
persona1.show_persona() 


hs1.creaTabella() 
