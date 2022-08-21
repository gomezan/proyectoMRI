
from abc import ABC, abstractmethod

class PosprocesamientoInterfaz(ABC):

    # Permite realizar el posprocesamiento sobre una imagen dada una estartegia
    @abstractmethod
    def prepararSalida(self, img, estrategia: str):
        pass