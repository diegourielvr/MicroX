class LoginController:
    def __init__(self, view, model, padre):
        self.view = view
        self.model = model
        self.padre = padre
        self.init()
    def init(self):
        self.view.btn_login.clicked.connect(self.clickLogin)

    def clickLogin(self):
        user = self.view.field_usuario.text()
        pw = self.view.field_contrasena.text()
        if self.model.validUserAndPass(user, pw):
            print("Existe en la base de datos")
            return
        print("No existe en la base de datos")
        return



    def mostrar(self):
        self.view.show()


