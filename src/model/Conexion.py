from ENV import *
import mysql.connector

from src.model.Cua import Cua
from src.model.Usuario import Usuario
from src.model.dbModel.DBCuas import DBCuas
from src.model.dbModel.DBLogs import DBLogs
from src.model.dbModel.DBUsuarios import DBUsuarios


class Conexion:
    def __init__(self):
        self.dbUsuarios = DBUsuarios()
        self.dbCuas = DBCuas()
        self.dbLogs = DBLogs()

    def validUserAndPass(self, usuario, contrasena):
        res = self.dbUsuarios.validUserAndPass(usuario, contrasena)
        if res:
            self.dbLogs.agregarLog(usuario, "[LOGIN CORRECTO]", f"{usuario} con id: {res} se logeo")
        else:
            self.dbLogs.agregarLog(usuario, "[LOGIN INCORRECTO]", f"{usuario} intento hacer login")
        return res

    def existeUsuario(self, username):
        res = self.dbUsuarios.existeUsuario(username)
        if res:
            self.dbLogs.agregarLog("SYSTEM", "[CONSULTA CORRECTA]", f"Existe el usuario {username}")
        else:
            self.dbLogs.agregarLog("SYSTEM", "[CONSULTA FALLIDA]", f"No existe el usuario {username}")
        return res

    def getUsuarioById(self, id_usuario):
        res = self.dbUsuarios.getUsuarioById(id_usuario)
        if res:
            self.dbLogs.agregarLog("SYSTEM", "[CONSULTA CORRECTA]", f"Se obtuvo el usuario con id: {id_usuario}")
        else:
            self.dbLogs.agregarLog("SYSTEM", "[CONSULTA FALLIDA]", f"No se encontro el usuario con id: {id_usuario}")
        return res

    def agregarUsuario(self, username, password, imagen):
        res = self.dbUsuarios.agregarUsuario(username, password, imagen)
        if res:
            self.dbLogs.agregarLog("SYSTEM", "[INSERTAR REGISTRO CORRECTO]", f"Se agrego el usuario {username} a la base de datos")
        else:
            self.dbLogs.agregarLog("SYSTEM", "[INSERTAR REGISTRO FALLIDO]", f"No pudo agregar el usuario {username} a la base de datos")
        return res

    def agregarCua(self, id_usuario, titulo, contenido, imagen):
        res = self.dbCuas.agregarCua(id_usuario, titulo, contenido, imagen)
        if res:
            self.dbLogs.agregarLog(f"{id_usuario}", "[AGREGAR CUA CORRECTAMENTE]", f"El usuario con id {id_usuario} ha agregado una publicacion")
        else:
            self.dbLogs.agregarLog(f"{id_usuario}", "[AGREGAR CUA FALLIDO]", f" El usuario con id {id_usuario} no pudo agregar una publicacion")
        return res

    def getCuas(self):
        res = self.dbCuas.getCuas()
        if res:
            self.dbLogs.agregarLog("SYSTEM", "[CONSULTA CUAS CORRECTA]", "Se obtuvo una lista de cuas")
        else:
            self.dbLogs.agregarLog("SYSTEM", "[CONSULTA CUAS FALLIDA]", "No se pudo obtener una lista de cuas")
        return res

    def getCuasByIdUsuario(self, id_usuario):
        res = self.dbCuas.getCuasByIdUsuario(id_usuario)
        if res:
            self.dbLogs.agregarLog("SYSTEM", "[CONSULTA CUAS CORRECTA]", f"So obtuvieron los cuas del usuario con id {id_usuario}")
        else:
            self.dbLogs.agregarLog("SYSTEM", "[CONSULTA CUAS FALLIDA]", f"No pudo obtener los cuas del usuario con id {id_usuario}")
        return res

    def getCuaById(self, id_cua):
        res = self.dbCuas.getCuaById(id_cua)
        if res:
            self.dbLogs.agregarLog("SYSTEM", "[CONSULTA CUA CORRECTA]", f"Se obtuvo el cua con id {id_cua}")
        else:
            self.dbLogs.agregarLog("SYSTEM", "[CONSULTA CUA FALLIDA]", f"No se pudo obtener el cua con id {id_cua}")
        return res

    def modificarCuaById(self, id_cua, titulo, contenido, imagen):
        res = self.dbCuas.modificarCuaById(id_cua, titulo, contenido, imagen)
        if res:
            self.dbLogs.agregarLog("SYSTEM", "[MODIFICAR CUA CORRECTO]", f"Se ha modificado el cua con id {id_cua}")
        else:
            self.dbLogs.agregarLog("SYSTEM", "[MODIFICAR CUA FALLIDO]", f"No se ha podido modificar el cua con id {id_cua}")
        return res

    def eliminarCuaById(self, id_cua):
        res = self.dbCuas.eliminarCuaById(id_cua)
        if res:
            self.dbLogs.agregarLog("SYSTEM", "[ELIMINAR CUA CORRECTAMENTE]", f"Se ha eliminado el cua con id {id_cua}")
        else:
            self.dbLogs.agregarLog("SYSTEM", "[ELIMINAR CUA FALLIDO]", f"No se ha podido eliminar el cua con id {id_cua}")
        return res

    def suscribirseCuas(self, observer):
        self.dbCuas.suscribirse(observer)
        self.dbLogs.agregarLog("SYSTEM", "[SUSCRITO A CUAS CORRECTAMENTE]", f"Un objeto se ha suscrito a las actualizaciones de dbCuas")

    def desuscribirseCuas(self, observer):
        self.dbCuas.desuscribirse(observer)
        self.dbLogs.agregarLog("SYSTEM", "[SUSCRIPCION ELIMINADA A CUAS CORRECTAMENTE]", f"Un objeto se ha desuscrito a las actualizaciones de dbCuas")
