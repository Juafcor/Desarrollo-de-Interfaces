from abc import ABC, abstractmethod
from typing import List


# Excepción personalizada
class PlantaException(Exception):
    def __init__(self, mensaje: str):
        super().__init__(mensaje)

# Clase abstracta Planta
class Planta(ABC):
    def __init__(self, nombre: str, altura: int, precio: float) -> None:
        self._nombre = nombre
        self.setAltura(altura)
        self.setPrecio(precio)

    def getNombre(self) -> str:
        return self._nombre

    def setNombre(self, nombre: str) -> None:
        self._nombre = nombre

    def getAltura(self) -> int:
        return self._altura

    def setAltura(self, altura: int) -> None:
        if altura < 5 or altura > 300:
            raise PlantaException("La altura debe estar entre 5 y 300 cm")
        self._altura = altura

    def getPrecio(self) -> float:
        return self._precio

    def setPrecio(self, precio: float) -> None:
        if precio <= 0:
            raise PlantaException("El precio debe ser mayor que 0")
        self._precio = precio

    @abstractmethod
    def getDescripcion(self) -> str:
        pass


# Subclase Cactus
class Cactus(Planta):
    def __init__(self, nombre: str, altura: int, precio: float, tieneEspinas: bool) -> None:
        super().__init__(nombre, altura, precio)
        self._tieneEspinas = tieneEspinas

    def isTieneEspinas(self) -> bool:
        return self._tieneEspinas

    def setTieneEspinas(self, tieneEspinas: bool) -> None:
        self._tieneEspinas = tieneEspinas

    def getDescripcion(self) -> str:
        return f"Cactus {'con espinas' if self._tieneEspinas else 'sin espinas'}"


# Subclase Flor
class Flor(Planta):
    def __init__(self, nombre: str, altura: int, precio: float, color: str) -> None:
        super().__init__(nombre, altura, precio)
        self._color = color

    def getColor(self) -> str:
        return self._color

    def setColor(self, color: str) -> None:
        self._color = color

    def getDescripcion(self) -> str:
        return f"Flor {self._color}"

