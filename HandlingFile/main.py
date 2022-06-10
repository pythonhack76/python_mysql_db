#gestione dei files
import os

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


def leggiFiles():
    select_dir = input("indica tu la directory...")
    if select_dir != True:
        current_directory = os.getcwd()
        files = os.listdir(current_directory)
        for filename in files:
            print(filename)
    else:
        files = os.listdir(select_dir)
        for filename in files:
            print(filename)
        


leggiFiles() 