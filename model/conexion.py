import mysql.connector

class DataBase:
    def __init__(self):
        self.connection=mysql.connector.connect(
            host= "localhost",
            user= "root",
            password="12345678",
            database="bdegresados"
        )
        self.cursor=self.connection.cursor()
        
    def cerrar(self):
        self.cursor.close()
        self.connection.close()
