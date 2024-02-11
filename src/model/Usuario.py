class Usuario:
    def __init__(self, id_usuario, username, ruta_avatar):
        self.id_usuario = id_usuario
        self.username = username
        self.ruta_avatar = ruta_avatar

    def getIdUsuario(self):
        return self.id_usuario

    def getNombreUsuario(self):
        return self.username