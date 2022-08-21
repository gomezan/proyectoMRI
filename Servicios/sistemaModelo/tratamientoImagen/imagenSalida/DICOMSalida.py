
from tratamientoImagen.imagenSalida.EstrategiaConversionImagenesSalida import EstrategiaConversionImagenesSalida

class DICOMSalida(EstrategiaConversionImagenesSalida):

    def __init__(self):
        self.__SIZE=256

    def convertirSalida(self, img):
        return img