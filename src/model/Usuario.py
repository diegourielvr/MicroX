class Usuario:
    def __init__(self, id_usuario, username, avatar):
        self.id_usuario = id_usuario
        self.username = username
        self.avatar = avatar # Binario

    def getIdUsuario(self):
        return self.id_usuario

    def getNombreUsuario(self):
        return self.username