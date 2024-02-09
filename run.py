import sys
from PyQt6.QtWidgets import QApplication
from src.view.login.GUI_Login import GUI_Login
from src.controller.login.LoginController import LoginController

def main():
    app = QApplication(sys.argv)
    loginView = GUI_Login()
    loginController = LoginController(loginView, None, None)
    loginController.mostrar()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()