import os

files = []
path = "E:\Python\Python_course\Files"
def createFile():
    file = "news2.txt"
    with open(file, mode='x', encoding='utf-8') as f:
        f.write('come iniziare a scrivere codice malevole')

    try:
        if file != 0:
            print("file esistente")
            for lines in file:
                print(lines, '\n')
                files.append
                print("ho aggiunto un file")
        else:
            print("creo un nuovo file?")
            
    except: 
        print("errore")

def leggiFile():
    with open(file, mode='r', encoding='utf-8') as f:
        for line in f:
            print(line, end = '')
def readFile():
    for file in files:
        print(file, '\n')

readFile() 