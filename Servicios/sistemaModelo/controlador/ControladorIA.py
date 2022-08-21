
#modelos de red neuronal
from modelo.RedNeuronal import RedNeuronal

#interfaces de integracion
from integracion.FachadaIntegracionInterfaz import FachadaIntegracionInterfaz

#Procesamiento de imágenes
from tratamientoImagen.FachadaProcesamientoInterfaz import FachadaProcesamientoInterfaz

#librerias uti

class ControladorIA:

    def __init__(self, modelo: RedNeuronal, procesador: FachadaProcesamientoInterfaz, integracion: FachadaIntegracionInterfaz):
        # A través de inyección de dependencias se tiene:
        # Modelo de super-resolución
        self.__srNN= modelo
        # Modulo de procesamiento de la imagen
        self.__pro=procesador
        # Modulo de integración
        self.__int=integracion
        print("nací")

    # Dada una imagen se encarga de realizar la super-resolución de esta.
    def predecirImagen(self, img):
        return self.__srNN.predecirImagen(img)

    # se encarga de todo el pre-procecamiemto de la imagen dada una estrategia esecifica
    # Antes de realizar la super-resoluación
    def procesarImagenEntrada(self , img, estrategia):
        return self.__pro.prepararEntrada(img, estrategia)

    # se encarga de todo el pos-procecamiemto de la imagen  dada una estrategia especifica
    # Despues de realizar la super-resoluación
    def procesarImagenSalida(self , img, estrategia):
        return self.__pro.prepararSalida(img, estrategia)

    # Obtiene una imagen especifica dada la llave del S3
    def buscarImagen(self, s3_key):
        return self.__int.download_data(s3_key)


    # Descarga directamente al computador una imagen del S3
    def descargarImagen(self, s3_key,path):
        return self.__int.download_file(s3_key,path)

    # Carga una imagen a S3
    def cargarImagen(self, img, path):
        return self.__int.upload_data_to_bucket(img, path)

    # Permite solicitar información de la próxima imagen a tratar
    def solicitarPaquete(self):
        self.__int.solicitarPaquete()

    #Solicita la llave del s3 de la imagen cuyo paquete se ha obtenido previamente
    def solicitarImagen(self):
        return self.__int.obtenerImagen()

    #Permite actualizar de la información de la imagen tratada
    def actualizarPaquete(self, infoProcesada):
        self.__int.actualizarPaquete(infoProcesada)

    # Se desconecta de la cola
    def desconectar(self):
        self.__int.desconectar()













