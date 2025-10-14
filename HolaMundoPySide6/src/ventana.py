from PySide6.QtWidgets import QWidget, QLabel

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana")
        self.etiqueta1 = QLabel("Hola mundo!", self)
