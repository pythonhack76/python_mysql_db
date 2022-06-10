#gestione dei files

def creaFile():
    global file
    file = input("nome del file:")
    f = open(file, "w")
    f.write("contenuti nuovi")
    f.close()

def leggiFile():
    f = open(file, "r")
    print(f.read())
    f.close() 


creaFile()
leggiFile() 