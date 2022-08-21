
from abc import ABC, abstractmethod

class PreprocesamientoInterfaz(ABC):


    # Función encargada de pre-procesar la imagen
    @abstractmethod
    def prepararEntrada(self, img, estrategia: str):
        pass