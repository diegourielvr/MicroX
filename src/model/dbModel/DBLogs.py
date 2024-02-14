import mysql.connector
from ENV import USER_LOG, HOST_LOG, PASSWORD_LOG, DATABASE_LOG
from src.patrones.Singleton import singleton

@singleton
class DBLogs(object):
    def __init__(self):
        # Conectar a la base de datos MySQL
        self.connection = mysql.connector.connect(
            host = HOST_LOG,
            user = USER_LOG,
            password = PASSWORD_LOG,
            database= DATABASE_LOG
        )
        self.cursor = self.connection.cursor()

    def agregarLog(self, username, movimiento, contenido):
        try:
            sql = """
            INSERT INTO logs (username, movimiento, contenido)
            VALUES (%s, %s, %s)
            """
            values = (username, movimiento, contenido)
            self.cursor.execute(sql, values)
            self.connection.commit()
            if self.cursor.rowcount:
                return True
        except mysql.connector.Error as err:
            return False
