
from abc import ABC, abstractmethod

class CtrDtoInterfaz(ABC):

    # Permite modificar el paqueteque almacena el controlador
    @abstractmethod
    def almacenarPaquete(self, paquete):
        pass

    #Permite modificar la información que contiene el paquete
    @abstractmethod
    def actualizarPaquete(self, infoProcesada):
        pass

    # Devuelve la llave s3 de una imagen especificada
    @abstractmethod
    def solicitarURLImagen(self):
        pass

    # Permite obtener todo el paquete
    @abstractmethod
    def getPaquete(self):
        pass

    # Deshecha el paquete actual
    @abstractmethod
    def vaciarPaquete(self):
        pass