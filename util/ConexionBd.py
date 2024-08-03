import mysql.connector

class ConexionBd:
    
    def __init__(self) -> None:
        self.conexion = mysql.connector.connect(host='localhost',
                                                database='bdnotas',
                                                user='root',
                                                password='123456')
    
    def getConexionBD(self):
        return self.conexion