class Cua:
    def __init__(self, id_cua, id_usuario, titulo, contenido, imagen, fecha_modificacion):
        self.id_cua = id_cua
        self.id_usuario = id_usuario
        self.titulo = titulo
        self.contenido = contenido
        self.imagen = imagen # Bytes
        self.fecha_modificacion = fecha_modificacion

    def getIdCua(self):
        return self.id_cua

    def getIdUsuario(self):
        return self.id_usuario

    def getTitulo(self):
        return self.titulo

    def getContenido(self):
        return self.contenido

    def getImagen(self):
        return self.imagen

    def getFechaModificacion(self):
        return self.fecha_modificacion

    def getFechaModificacionToString(self):
        return self.fecha_modificacion.strftime("%Y-%m-%d %H:%M:%S")  # str
