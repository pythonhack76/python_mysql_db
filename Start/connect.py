class Connessione:
    def __init__(self, db, username, password, port, table):
        self.db = db
        self.username = username
        self.password = password
        self.port = port
        self.table = table 


    def creaTabella(self):
        print("la tabella dobbiamo ancora crearla")


    def insertItems(self):
        pass

    def updateItems(self):
        pass




hs1 = Connessione('%s','%s','%s','%s','%s')
    