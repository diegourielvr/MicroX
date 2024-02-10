from ENV import *
import mysql.connector

class Registro:
    def __init__(self):
        # Conectar a la base de datos MySQL
        self.connection = mysql.connector.connect(
            host = HOST,
            user = USER,
            password = PASSWORD,
            database= DATABASE
        )
        self.cursor = self.connection.cursor()

    def addUser(self, user, pw):
        try:
            # Insertar el nuevo usuario en la base de datos
            sql = "INSERT INTO usuarios (nombre_usuario, contrasena) VALUES (%s, %s)"
            values = (user, pw)
            self.cursor.execute(sql, values)
            self.connection.commit()
            return True
        except mysql.connector.Error as err:
            return False
