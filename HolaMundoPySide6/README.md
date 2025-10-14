# Mi primer “Hola Mundo” con PySide6

## 1. Contexto y propósito
En este proyecto crearemos nuestra **primera aplicación de escritorio en Python** utilizando **PySide6**, el binding oficial de **Qt para Python**.  

 [**Repositorio del proyecto**](https://github.com/Juafcor/Desarrollo-de-Interfaces/edit/main/HolaMundoPySide6/)

---

## .2 Objetivos

- Crear y activar un entorno virtual (`venv`) de Python.  
- Instalar dependencias mediante `pip`.  
- Comprender el rol de **QApplication** y el bucle de eventos (`app.exec()`).  
- Crear una ventana básica con **PySide6** que muestre “Hola Mundo”.  
- Separar el código en módulos (`main.py` y `ventana.py`).  
- Ejecutar y probar la aplicación.

---

## 3. Requisitos previos

| Recurso | Versión / Recomendación |
|----------|-------------------------|
| **Python** | 3.11 o superior |
| **Sistema operativo** | Windows 10/11 |
| **Editor recomendado** | Visual Studio Code |
| **Herramientas** | Git, terminal / consola del sistema |

Verifica la versión de Python instalada:

```
python --version
```



## 4. Creación y activación del entorno virtual

Comandos a utilizar para la instalación y activación del entorno virtual:

```

python -m venv venv
venv\Scripts\activate

```
Al poner venv 2 veces, estamos creando el entorno y dándole un nombre. Si en vez de venv venv ponemos venv miVenv, estaremos creando un entorno llamado miVenv.

Para confirmar el entorno y el intérprete, ponemos: 
```
where python
```



## 5. Instalación de PySide6

Una vez estemos ya dentro del entorno virtual, queremos utilizar PySide6. Para ello pondremos en la terminal lo siguiente:

```
pip install PySide6
```

Ahora queremos exportar los requirimientos del entorno virtual para ejecutar el archivo, en este caso las librerías que hemos instalado:

```
 pip freeze > requirements.txt
```
### ¿Qué es PySide6 y por qué queremos usarlo?
[PySide6](https://doc.qt.io/qtforpython/) es un conjunto de bindings de Qt para Python que permite crear interfaces gráficas de usuario (GUIs) modernas, potentes y multiplataforma.
Es una alternativa oficial a PyQt y permite crear ventanas, botones, menús, cuadros de texto, etc.


## 6. Estructura del proyecto
 proyecto-hola-mundo/
 ├─ src/
 │  ├─ main.py          # punto de entrada
 │  └─ ventana.py       # clase Ventana
 ├─ .gitignore
 ├─ requirements.txt
 └─ README.md


## 7. Código fuente

El código utilizado es el siguiente: 
Clase ventana:
```
from PySide6.QtWidgets import QWidget, QLabel

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana")
        self.etiqueta1 = QLabel("Hola mundo!", self)

```
Main:

```
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

```
