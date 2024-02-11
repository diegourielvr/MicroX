class VPubController:
    def __init__(self, view, model, padre):
        self.view = view
        self.model = model
        self.padre = padre

    def mostrar(self):
        self.view.show()