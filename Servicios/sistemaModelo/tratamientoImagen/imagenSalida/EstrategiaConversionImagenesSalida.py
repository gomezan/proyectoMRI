

from abc import ABC, abstractmethod

class EstrategiaConversionImagenesSalida(ABC):

    # Método encargado de realizar la converción de numpy al formato de salida
    @abstractmethod
    def convertirSalida(self, img):
        pass