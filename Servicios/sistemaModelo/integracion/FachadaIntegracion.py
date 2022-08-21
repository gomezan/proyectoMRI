
#utils
from dataclasses import dataclass

from integracion.FachadaIntegracionInterfaz import FachadaIntegracionInterfaz
from integracion.sistemaArchivos.AdaptadorSistemaArchivosInterfaz import AdaptadorSistemaArchivosInterfaz
from integracion.sistemaArchivos.AdaptadorSistemaArchivos import AdaptadorSistemaArchivos
from integracion.back.AdaptadorBackInterfaz import AdaptadorBackInterfaz
from integracion.back.AdaptadorBack import AdaptadorBack
from integracion.back.cola.AdaptadorActiveMQInterfaz import AdaptadorActiveMQInterfaz
from integracion.back.cola.AdaptadorActiveMQ import AdaptadorActiveMQ

@dataclass
class FachadaIntegracion(FachadaIntegracionInterfaz):

    # La fachada de integración controla dos modulos:
    # Modulo encargado de la comunicación con el sistema S3
    sistemaArchivos: AdaptadorSistemaArchivosInterfaz = AdaptadorSistemaArchivos()
    # Modulo encargado de la comunicación con el back
    back: AdaptadorBackInterfaz = AdaptadorBack()

    def download_data(self, s3_key):
        return self.sistemaArchivos.download_data_from_bucket(s3_key)

    def download_file(self, s3_key, dst_path):
        return self.sistemaArchivos.download_file_from_bucket(s3_key, dst_path)

    def upload_data_to_bucket(self, bytes_data, s3_key):
        return self.sistemaArchivos.upload_data_to_bucket(bytes_data, s3_key)

    def obtenerImagen(self):
        return self.back.obtenerImagen()

    def solicitarPaquete(self):
        self.back.solicitarPaquete()

    def actualizarPaquete(self, infoProcesada):
        self.back.actualizarPaquete(infoProcesada)

    def desconectar(self):
        return self.back.desconectar()