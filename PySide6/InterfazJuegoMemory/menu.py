import sys, random
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QGridLayout, QMainWindow, QPushButton
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

from carta import Carta


class MemoryUI(QMainWindow):
    def __init__(self):
        super().__init__()
        boton_facil = None
        boton_medio = None
        boton_dificil = None
        
        self.setWindowTitle("EL MEMORY")
        self.setFixedSize(700, 600)
    
        imagenes = [
            "src/img/sans.jpg", "src/img/deltarune.jpg", "src/img/heartbound.jpg",
            "src/img/heartbound.jpg", "src/img/deltarune.jpg", "src/img/tboiRepentance.jpg",
            "src/img/ness.png", "src/img/hollow_knight.png", "src/img/hollow_knight.png",
            "src/img/tboiRepentance.jpg", "src/img/ness.png", "src/img/sans.jpg"
        ]
        random.shuffle(imagenes)

        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout(central)

        title = QLabel("EL MEMORY")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 36px; font-weight: bold; letter-spacing: 4px;")
        main_layout.addWidget(title)

        top_layout = QHBoxLayout()
        main_layout.addLayout(top_layout)

        cartas_layout = QGridLayout()
        top_layout.addLayout(cartas_layout, 3)

        index = 0
        for fila in range(3):
            for col in range(4):
                carta = Carta(imagenes[index])
                cartas_layout.addWidget(carta, fila, col)
                index += 1

        panel_layout = QVBoxLayout()
        top_layout.addLayout(panel_layout, 1)

        marcador_label = QLabel("Intentos")
        marcador_label.setAlignment(Qt.AlignCenter)
        marcador_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        panel_layout.addWidget(marcador_label)

        vidas_label = QLabel("3")
        vidas_label.setAlignment(Qt.AlignCenter)
        vidas_label.setStyleSheet("font-size: 35px; font-weight: bold;")
        panel_layout.addWidget(vidas_label)

        for i in range(3):
            corazon = QLabel()
            pixmap = QPixmap("src/img/vida.png").scaled(70, 70, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            corazon.setPixmap(pixmap)
            corazon.setAlignment(Qt.AlignCenter)
            panel_layout.addWidget(corazon)

        panel_layout.addStretch()

        bot_layout = QHBoxLayout()
        main_layout.addLayout(bot_layout)

        nivel_label = QLabel("Nivel:")
        nivel_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        boton_facil = QPushButton("EASY")
        boton_medio = QPushButton("MEDIUM")
        boton_dificil = QPushButton("HARD")
        bot_layout.addWidget(nivel_label)
        bot_layout.addWidget(boton_facil)
        bot_layout.addWidget(boton_medio)
        bot_layout.addWidget(boton_dificil)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MemoryUI()
    window.show()
    sys.exit(app.exec())
