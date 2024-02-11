import sys
from PyQt6.QtWidgets import QApplication
from src.controller.MasterController import MasterController

def main():
    app = QApplication(sys.argv)
    masterController = MasterController()
    masterController.mostrarLogin()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()