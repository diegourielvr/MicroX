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
        rows = self.cursor.fetchall() # fetchall devuelve una lista de tuplas
        if rows:
            return rows[0][0] # id_usuario
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
            SELECT id_usuario, username, imagen FROM usuarios
            WHERE id_usuario = %s
            """
            values = (id_usuario, )
            self.cursor.execute(sql, values)
            result = self.cursor.fetchone() # fetchone devuelve primera fila del resultado
            if result:
                usuario = Usuario(result[0], result[1], result[2])
                return usuario
            return None
        except mysql.connector.Error as err:
            return None

    def agregarUsuario(self, username, password, imagen):
        """Imagen es de tiop binario
        """
        try:
            sql = """
            INSERT INTO usuarios (username, password, imagen)
            VALUES (%s, %s, %s)
            """
            values = (username, password, imagen)
            self.cursor.execute(sql, values)
            self.connection.commit()
            # self.cursor.rowcount:
        except mysql.connector.Error as err:
            return False
