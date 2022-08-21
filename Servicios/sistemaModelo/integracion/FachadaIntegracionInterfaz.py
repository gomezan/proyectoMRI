
from abc import ABC, abstractmethod

class FachadaIntegracionInterfaz(ABC):

    #Permite decargar una imagen del s3
    @abstractmethod
    def download_data(self, s3_key):
        pass

    # Permite decargar una imagen directamente al computador
    @abstractmethod
    def download_file(self, s3_key, dst_path):
        pass

    # Permite cargar una imagen al servidor s3
    @abstractmethod
    def upload_data_to_bucket(self, bytes_data, s3_key):
        pass

    # Permite obtener la llave del s3 de la imagen del paquete
    @abstractmethod
    def obtenerImagen(self):
        pass

    # Permite solciitar el paquete con la información de la imagen
    @abstractmethod
    def solicitarPaquete(self):
        pass

    # Permite enviar a la cola un paquete con la información actualizada de una imagen
    @abstractmethod
    def actualizarPaquete(self, infoProcesada):
        pass

    # Desconectar con la cola al back
    @abstractmethod
    def desconectar(self):
        pass