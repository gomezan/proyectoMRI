
from abc import ABC, abstractmethod

class RedNeuronal(ABC):

    # Este método permite dad una imagen realizar el proceso de super resolución
    @abstractmethod
    def predecirImagen(self, img):
        pass





