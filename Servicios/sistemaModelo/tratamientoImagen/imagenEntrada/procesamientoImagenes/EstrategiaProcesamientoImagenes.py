
from abc import ABC, abstractmethod

class EstrategiaProcesamientoImagenes(ABC):


    # Se encarga de preparar la imagen para la red.
    @abstractmethod
    def procesar(self, img):
        pass