from ENV import *
import mysql.connector

from src.model.Cua import Cua
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
        """DEvuelve un objeto de tipo Usuario"""
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
        """Imagen es de tipo binario
        """
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
        except mysql.connector.Error as err:
            return False

    def agregarCua(self, id_usuario, titulo, contenido, imagen):
        """Imagen es de tipo binario
        """
        try:
            sql = """
            INSERT INTO cuas (id_usuario, titulo, contenido, imagen)
            VALUES (%s, %s, %s, %s)
            """
            values = (id_usuario, titulo, contenido, imagen)
            self.cursor.execute(sql, values)
            self.connection.commit()
            if self.cursor.rowcount:
                return True
        except mysql.connector.Error as err:
            return False

    def getCuasResumen(self):
        """TODO:Devuelve una lista de objetos Cuas con todas las cuas almanecedas"""
        try:
            sql = """
            SELECT id_cua, id_usuario, titulo, contenido
            FROM cuas
            ORDER BY fecha_modificacion DESC
            """
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()  # fetchall devuelve una lista de tuplas
            if rows:
                return rows
            return None
        except mysql.connector.Error as err:
            return None

    def getCuasByIdUsuario(self, id_usuario):
        """TODO:Devuelve una lista de Cuas que pertenecen al usuario con id id_usuario"""
        try:
            sql = """
            SELECT id_cua, titulo, contenido, imagen, fecha_modificacion FROM cuas
            WHERE id_usuario = %s
            ORDER BY fecha_modificacion DESC
            """
            values = (id_usuario, )
            self.cursor.execute(sql, values)
            result = self.cursor.fetchall()
            if result:
                return result
            return None
        except mysql.connector.Error as err:
            return None

    def getCuaById(self, id_cua):
        """Devuelve un objeto de tipo Cua
        """
        try:
            sql = """
            SELECT * FROM cuas
            WHERE id_cua = %s
            """
            values = (id_cua, )
            self.cursor.execute(sql, values)
            res = self.cursor.fetchone()
            if res:
                cua = Cua(res[0], res[1], res[2], res[3], res[4], res[5])
                return cua
            return None
        except mysql.connector.Error as err:
            return None

    def modificarCuaById(self, id_cua, titulo, contenido, imagen):
        try:
            sql = """
            UPDATE cuas
            SET titulo = %s,
            contenido = %s,
            imagen = %s
            WHERE id_cua = %s
            """
            values = (titulo, contenido, imagen, id_cua)
            self.cursor.execute(sql, values)
            self.connection.commit()
            if self.cursor.rowcount:
                return True
        except mysql.connector.Error as err:
            return None

