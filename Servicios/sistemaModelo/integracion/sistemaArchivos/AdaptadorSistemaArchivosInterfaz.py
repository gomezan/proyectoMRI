
from abc import ABC, abstractmethod

class AdaptadorSistemaArchivosInterfaz(ABC):

    # con este se descarga, decodifica y se utiliza en memoria
    @abstractmethod
    def download_data_from_bucket(self, s3_key):
        pass

    # con este solo se descarga y se guarda directamente en memoria
    @abstractmethod
    def download_file_from_bucket(self, s3_key, dst_path):
        pass

    # subir imagenes al s3
    @abstractmethod
    def upload_data_to_bucket(self, bytes_data, s3_key):
        pass

