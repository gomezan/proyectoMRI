
from abc import ABC, abstractmethod

class EstrategiaConversionImagenesEntrada(ABC):


    # Se encarga de convertir una imagen de entrada a formato numpy.
    @abstractmethod
    def convertirEntrada(self, img):
        pass
