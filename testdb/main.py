import mysql.connector
from mysql.connector import cursor 

db = mysql.connector.connect(
    host="localhost",
    port = 3307,
    user="root",
    password="root",
    database="pysql"
)


cursor = db.cursor() 

sql = "SELECT \
    nome, cognome, citta.nome_citta \
    FROM clienti \
    INNER JOIN citta ON clienti.citta = id_citta "

cursor.execute(sql)
result = cursor.fetchall()

for riga in result: 
    print(riga)