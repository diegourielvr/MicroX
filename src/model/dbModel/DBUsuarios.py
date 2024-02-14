import mysql.connector

from ENV import USER, HOST, PASSWORD, DATABASE
from src.model.Usuario import Usuario
from src.patrones.Singleton import singleton


@singleton
class DBUsuarios(object):
    def __init__(self):
        # Conectar a la base de datos MySQL
        self.connection = mysql.connector.connect(
            host = HOST,
            user = USER,
            password = PASSWORD,
            database = DATABASE
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
        try:
            self.cursor.execute(sql, values)
            rows = self.cursor.fetchall()  # fetchall devuelve una lista de tuplas
            if rows:
                return rows[0][0]  # id_usuario
            return False
        except mysql.connector.Error as err:
            return None

    def existeUsuario(self, username):
        sql = """
        SELECT id_usuario FROM usuarios
        WHERE username = %s
        """
        values = (username, )
        try:
            self.cursor.execute(sql, values)
            rows = self.cursor.fetchall()
            if rows:
                return True
            return False
        except mysql.connector.Error as err:
            return None


    def getUsuarioById(self, id_usuario):
        """DEvuelve un objeto de tipo Usuario"""
        sql = """
        SELECT id_usuario, username, imagen FROM usuarios
        WHERE id_usuario = %s
        """
        values = (id_usuario, )
        try:
            self.cursor.execute(sql, values)
            result = self.cursor.fetchone()  # fetchone devuelve primera fila del resultado
            if result:
                usuario = Usuario(result[0], result[1], result[2])
                return usuario
            return False
        except mysql.connector.Error as err:
            return None


    def agregarUsuario(self, username, password, imagen):
        """Imagen es de tipo binario
        """
        if not isinstance(username, str) or not isinstance(password, str) or not isinstance(imagen, bytes):
            return False

        if username.isspace() or password.isspace():
            return False

        try:
            sql = """
            INSERT INTO usuarios (username, password, imagen)
            VALUES (%s, %s, %s)
            """
            values = (username, password, imagen)
            self.cursor.execute(sql, values)
            self.connection.commit()
            if self.cursor.rowcount:
                return True
            return False
        except mysql.connector.Error as err:
            return None
