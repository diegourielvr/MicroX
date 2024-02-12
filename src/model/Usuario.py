class Usuario:
    def __init__(self, id_usuario, username, avatar):
        self.id_usuario = id_usuario
        self.username = username
        self.avatar = avatar # Binario BLOB

    def getIdUsuario(self):
        return self.id_usuario

    def getUsername(self):
        return self.username

    def getAvatar(self):
        """Devolver el avatar del usuario

        Returns:
            avatar: bytes (Blob)
        """
        return self.avatar