class VPubDeleteController:
    def __init__(self, view, model, padre):
        self.view = view
        self.model = model
        self.padre = padre
        self.id_cua = None

    def setIdCua(self, id_cua):
        self.id_cua = id_cua

    def eliminar(self):
        self.model.eliminarCuaById(self.id_cua)
        self.padre.mostrar()
        self.view.hide()

    def cancelar(self):
        self.padre.mostrar()

    def mostrar(self):
        self.view.show()
