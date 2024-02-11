class LoginController:
    def __init__(self, view, model, padre):
        self.view = view
        self.model = model
        self.padre = padre

    def login(self, usuario, contrasena):
        """Validar datos de login e iniciar sesion

        """
        if not usuario or not contrasena:
            self.view.setEstado("Llena los campos")
            return

        id_usuario = self.model.validUserAndPass(usuario, contrasena)
        if id_usuario:
            print("existe en la base de datos")
            user = self.model.getUsuarioById(id_usuario)
            self.padre.setUsuario(user)
            self.padre.mostrarVPub()
            self.view.hide()
            # ocultar o destruir ventana de login
        else:
            print("No existe en la base de datos")

    def registrarse(self):
        """Mostrar ventana para registrar un nuevo usuario

        """
        self.padre.mostrarRegistrarse()
        self.view.limpiarCampos()
        self.view.hide()

    def mostrar(self):
        """Mostrar la ventana de login

        """
        self.view.show()


