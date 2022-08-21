

from abc import ABC, abstractmethod

class FachadaProcesamientoInterfaz(ABC):

    # Prepara la imagen de la entrada antes de la super-resolución
    @abstractmethod
    def prepararEntrada(self, img, estrategia: str):
        pass

    # Prepara la imagen despues de la super-resolución
    @abstractmethod
    def prepararSalida(self, img, estrategia: str):
        pass