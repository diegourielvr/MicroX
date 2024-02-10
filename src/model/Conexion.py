from ENV import *
import mysql.connector

class Conexion:
    def __init__(self):
        # Conectar a la base de datos MySQL
        self.connection = mysql.connector.connect(
            host = HOST,
            user = USER,
            password = PASSWORD,
            database= DATABASE
        )
        self.cursor = self.connection.cursor()

    def validUserAndPass(self, user, pw):
        sql = f"""
        SELECT * FROM usuarios
        WHERE nombre_usuario = %s
        AND contrasena = %s
        """
        values = (user, pw)
        self.cursor.execute(sql, values)
        rows = self.cursor.fetchall()
        if rows:
            return True
        return False
        
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
