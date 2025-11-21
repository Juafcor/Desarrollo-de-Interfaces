from PySide6.QtWidgets import QWidget, QLabel, QStackedLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class Carta(QWidget):
    def __init__(self, imagen_frente, imagen_reverso="src/img/anverso.jpg"):
        super().__init__()

        # Layout apilado (reverso / frente)
        self.layout = QStackedLayout(self)

        # Imagen del reverso
        self.label_reverso = QLabel()
        pixmap_reverso = QPixmap(imagen_reverso).scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label_reverso.setPixmap(pixmap_reverso)
        self.label_reverso.setAlignment(Qt.AlignCenter)

        # Imagen del frente
        self.label_frente = QLabel()
        pixmap_frente = QPixmap(imagen_frente).scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label_frente.setPixmap(pixmap_frente)
        self.label_frente.setAlignment(Qt.AlignCenter)

        # Añadir ambos al layout
        self.layout.addWidget(self.label_reverso)
        self.layout.addWidget(self.label_frente)

        # Mostrar primero el reverso
        self.mostrando_frente = False
        self.layout.setCurrentIndex(0)

        # Conectar clic
        self.mousePressEvent = self.voltear

    def voltear(self, event):
        """Voltea la carta entre frente y reverso"""
        self.mostrando_frente = not self.mostrando_frente
        self.layout.setCurrentIndex(1 if self.mostrando_frente else 0)
