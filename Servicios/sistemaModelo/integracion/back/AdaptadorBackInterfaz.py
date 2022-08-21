
from abc import ABC, abstractmethod

class AdaptadorBackInterfaz(ABC):

    # Permite obtener la llave del s3 de la imagen del paquete
    @abstractmethod
    def obtenerImagen(self):
        pass

    # Permite solciitar el paquete con la información de la imagen
    @abstractmethod
    def solicitarPaquete(self):
        pass

    # Permite modificar la información
    @abstractmethod
    def actualizarPaquete(self, infoProcesada):
        pass