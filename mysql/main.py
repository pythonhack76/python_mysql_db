parola_ordine = 'stringa'

print(parola_ordine)

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root", 
    database="newsql",
    port=3307
   

)

# cursor = db.cursor()
# cursor.execute("CREATE TABLE clienti (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR (255) )")
# cursor.execute("CREATE DATABASE newsql")
# cursor.execute("SHOW DATABASES")

# for x in cursor:
#     print(x)

cursor = db.cursor()

sql = "INSERT INTO clienti (nome, cognome) VALUES (%s, %s)"
values = ("roller","piano")
    
cursor.execute(sql, values)

db.commit()

print("id riga inserta: ", cursor.lastrowid)


