from PySide6.QtWidgets import QApplication
from ventana import Ventana

class App:
    def __init__(self):
        self.app = QApplication([])
        self.ventana = Ventana()

    def ejecutar(self):
        self.ventana.show()
        self.app.exec()

if __name__ == "__main__":
    aplicacion = App()
    aplicacion.ejecutar()
