import mysql.connector
from ENV import USER, HOST, PASSWORD, DATABASE
from src.model.Cua import Cua
from src.patrones.Observable import Observable
from src.patrones.Singleton import singleton

@singleton
class DBCuas(Observable, object):
    def __init__(self):
        Observable.__init__(self)
        # Conectar a la base de datos MySQL
        self.connection = mysql.connector.connect(
            host = HOST,
            user = USER,
            password = PASSWORD,
            database= DATABASE
        )
        self.cursor = self.connection.cursor()

    def agregarCua(self, id_usuario, titulo, contenido, imagen):
        """Imagen es de tipo binario
        """
        sql = """
        INSERT INTO cuas (id_usuario, titulo, contenido, imagen)
        VALUES (%s, %s, %s, %s)
        """
        values = (id_usuario, titulo, contenido, imagen)
        try:
            self.cursor.execute(sql, values)
            self.connection.commit()
            if self.cursor.rowcount:
                self.notificar()
                return True
            return False
        except mysql.connector.Error as err:
            print("Error al agregar un cua")
            return None

    def getCuas(self):
        sql = """
        SELECT * FROM cuas
        ORDER BY fecha_modificacion DESC
        """
        try:
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()  # fetchall devuelve una lista de tuplas
            if resultado:
                cuas = list()
                for res in resultado:
                    cua = Cua(res[0], res[1], res[2], res[3], res[4], res[5])
                    cuas.append(cua)

                return cuas
            return False
        except mysql.connector.Error as err:
            print("Error al obtener cuas")
            return None

    def getCuasByIdUsuario(self, id_usuario):
        sql = """
        SELECT * FROM cuas
        WHERE id_usuario = %s
        ORDER BY fecha_modificacion DESC
        """
        values = (id_usuario, )
        try:
            self.cursor.execute(sql, values)
            resultado = self.cursor.fetchall()
            if resultado:
                cuas = list()
                for res in resultado:
                    cua = Cua(res[0], res[1], res[2], res[3], res[4], res[5])
                    cuas.append(cua)

                return cuas
            return False
        except mysql.connector.Error as err:
            print("Error al obtener los cuas de un usuario")
            return None

    def getCuaById(self, id_cua):
        """Devuelve un objeto de tipo Cua
        """
        sql = """
        SELECT * FROM cuas
        WHERE id_cua = %s
        """
        values = (id_cua,)
        try:
            self.cursor.execute(sql, values)
            res = self.cursor.fetchone()
            if res:
                cua = Cua(res[0], res[1], res[2], res[3], res[4], res[5])
                return cua
            return False
        except mysql.connector.Error as err:
            print("Error al obtener un cua")
            return None

    def modificarCuaById(self, id_cua, titulo, contenido, imagen):
        sql = """
        UPDATE cuas
        SET titulo = %s,
        contenido = %s,
        imagen = %s
        WHERE id_cua = %s
        """
        values = (titulo, contenido, imagen, id_cua)
        try:
            self.cursor.execute(sql, values)
            self.connection.commit()
            if self.cursor.rowcount:

                self.notificar()
                return True
            return False
        except mysql.connector.Error as err:
            print("Error al modificar un cua")
            return None

    def eliminarCuaById(self, id_cua):
        try:
            sql = """
            DELETE FROM cuas
            WHERE id_cua = %s
            """
            values = (id_cua, )
            self.cursor.execute(sql, values)
            self.connection.commit()
            if self.cursor.rowcount:

                super().notificar()
                return True
            return False
        except mysql.connector.Error as err:
            print("Error al eliminar un cua")
            return None
