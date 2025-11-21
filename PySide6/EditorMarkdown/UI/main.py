from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QComboBox, QPushButton, QTextEdit, QFileDialog, QLabel
)
from PySide6.QtCore import Qt
import sys

class MarkdownEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor Markdown")
        self.resize(900, 600)

        layout = QVBoxLayout(self)

        # Primera fila: títulos, tablas, separador, códigos 
        fila1 = QHBoxLayout()
        self.combo_titulos = QComboBox()
        self.combo_titulos.addItems(["Título 1", "Título 2", "Título 3"])
        self.combo_titulos.setFixedHeight(60)

        self.combo_tablas = QComboBox()
        self.combo_tablas.addItems(["Tabla simple", "Tabla con bordes"])
        self.combo_tablas.setFixedHeight(60)

        btn_separador = QPushButton("Separador")
        btn_separador.setFixedHeight(60)

        fila1.addWidget(self.combo_titulos)
        fila1.addWidget(self.combo_tablas)
        fila1.addWidget(btn_separador)

        btnes_codigo=QVBoxLayout()

        btn_codigo_linea = QPushButton("Código línea")
        btn_codigo_bloque = QPushButton("Código bloque")

        btnes_codigo.addWidget(btn_codigo_bloque)
        btnes_codigo.addWidget(btn_codigo_linea)
        fila1.addLayout(btnes_codigo)
        
        layout.addLayout(fila1)

        # Segunda fila: botones negrita, cursiva, enlace, listas
        fila2 = QHBoxLayout()

        btn_negrita = QPushButton("Negrita")
        btn_cursiva = QPushButton("Cursiva")
        btn_enlace = QPushButton("Enlace")
        btn_negrita.setFixedHeight(60)
        btn_cursiva.setFixedHeight(60)
        btn_enlace.setFixedHeight(60)
        fila2.addWidget(btn_negrita)
        fila2.addWidget(btn_cursiva)
        fila2.addWidget(btn_enlace)

        btnes_listas= QVBoxLayout()

        btn_lista_ord = QPushButton("Lista ord")
        btn_lista_des = QPushButton("Lista desord")
        btnes_listas.addWidget(btn_lista_ord)
        btnes_listas.addWidget(btn_lista_des)

        fila2.addLayout(btnes_listas)    

        layout.addLayout(fila2)

        # Editor central
        self.editor = QTextEdit()
        layout.addWidget(self.editor)

        # Fila inferior: CARGAR y GUARDAR
        fila_inferior = QHBoxLayout()

        btn_cargar = QPushButton("Cargar")
        btn_cargar.clicked.connect(self.cargar_archivo)

        btn_guardar = QPushButton("Guardar")
        btn_guardar.clicked.connect(self.guardar_archivo)

        fila_inferior.addWidget(btn_cargar)
        fila_inferior.addWidget(btn_guardar)
        layout.addLayout(fila_inferior)

    def cargar_archivo(self):
        ruta, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Markdown (*.md);;Texto (*.txt)")
        if ruta:
            with open(ruta, "r", encoding="utf-8") as f:
                self.editor.setPlainText(f.read())

    def guardar_archivo(self):
        ruta, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", "", "Markdown (*.md);")
        if ruta:
            with open(ruta, "w", encoding="utf-8") as f:
                f.write(self.editor.toPlainText())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MarkdownEditor()
    ventana.show()
    sys.exit(app.exec())
