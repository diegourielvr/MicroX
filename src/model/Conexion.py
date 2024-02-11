from ENV import *
import mysql.connector

from src.model.Usuario import Usuario


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

    def validUserAndPass(self, usuario, contrasena):
        """Verificar si el usuario es valido

        :param usuario: str
        :param contrasena: str
        Returns:
            None: No existe o son incorrectos los datos
            id_usuario: str. El id del usuario
        """

        sql = """
        SELECT id_usuario FROM usuarios
        WHERE username = %s
        AND password = %s
        """
        values = (usuario, contrasena)
        self.cursor.execute(sql, values)
        rows = self.cursor.fetchall()
        if rows:
            return rows[0] # id_usuario
        return None

    def existeUsuario(self, username):
        sql = """
        SELECT id_usuario FROM usuarios
        WHERE username = %s
        """
        values = (username, )
        self.cursor.execute(sql, values)
        rows = self.cursor.fetchall()
        if rows:
            return True
        return False

    def getUsuarioById(self, id_usuario):
        try:
            sql = """
            SELECT id_usuario, username, ruta_avatar FROM usuarios
            WHERE id_usuario = %s
            """
            values = (id_usuario)
            self.cursor.execute(sql, values)
            rows = self.cursor.fetchall()
            if rows:
                usuario = Usuario(rows[0], rows[1], rows[2])
                return usuario
            return None
        except mysql.connector.Error as err:
            return None

    def agregarUsuario(self, username, password, ruta_avatar):
        try:
            sql = """
            INSERT INTO usuarios (username, password, ruta_avatar)
            VALUES (%s, %s, %s)
            """
            values = (username,password, ruta_avatar)
            self.cursor.execute(sql, values)
            self.connection.commit()
            if self.cursor.rowcount:
                return True
            return False
        except mysql.connector.Error as err:
            return False
