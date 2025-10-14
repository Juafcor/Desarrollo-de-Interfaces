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

```bash
python --version

```



## 4. Creación y activación del entorno virtual

Comandos a utilizar para la instalación y activación del entorno virtual:

```bash

python -m venv venv
venv\Scripts\activate

```
Al poner venv 2 veces, estamos creando el entorno y dándole un nombre. Si en vez de venv venv ponemos venv miVenv, estaremos creando un entorno llamado miVenv.

Para confirmar el entorno y el intérprete, ponemos: 
```bash
where python
```



## 5. Instalación de PySide6

Una vez estemos ya dentro del entorno virtual, queremos utilizar PySide6. Para ello pondremos en la terminal lo siguiente:

```
pip install PySide6


```
