parola_ordine = 'stringa'

print(parola_ordine)

import mysql.connector

class Db:
    def __init__(self, host, user, password, database, port):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port

        def Connessione(self, host, user, password, database, port):
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root", 
                database="newsql",
                port=3307  

            )
        def checkClass(self):
            elemento = print('verifica in corso della classe...')
            return elemento

# cursor = db.cursor()
# cursor.execute("CREATE TABLE clienti (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR (255) )")
# cursor.execute("CREATE DATABASE newsql")
# cursor.execute("SHOW DATABASES")

# for x in cursor:
#     print(x)

# cursor = db.cursor()
# sql = "SELECT * FROM clienti ORDER BY cognome DESC LIMIT 5"

# cursor.execute(sql)
# result = cursor.fetchall()

# for riga in result: 
#     print(riga)
    
 




# cursor = db.close()

    def Elimina(callback):

        db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root", 
        database="newsql",
        port=3307  

        )
        
        cursor = db.cursor()
        nome = "renzo"
        sql = "DELETE FROM clienti WHERE nome = %s"
        valore = (nome, )
        cursor.execute(sql, valore)
        db.commit() 

        print("numero di righe cancellate: ", cursor.rowcount)


    if __name__ == '__main__':
        Elimina(Connessione)


DefUno = Db()
DefUno.Elimina
DefUno.checkClass