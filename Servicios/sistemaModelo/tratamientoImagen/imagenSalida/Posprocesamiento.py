
from tratamientoImagen.imagenSalida.PosprocesamientoInterfaz import PosprocesamientoInterfaz
from tratamientoImagen.imagenSalida.EstrategiaConversionImagenesSalida import EstrategiaConversionImagenesSalida
from tratamientoImagen.imagenSalida.DICOMSalida import DICOMSalida
from tratamientoImagen.imagenSalida.NIFTISalida import NIFTISalida


class Posprocesamiento(PosprocesamientoInterfaz):

    # Permite relacionar un string con la estegia de pos-procesamiento
    def __init__(self):
        self.__estrategias={
           "DICOM": DICOMSalida(),
           "NIFTI": NIFTISalida()
        }

    # Función encargada de instanciar una estrategia especifica
    def leerEstrategia(self, estrategia: str) -> EstrategiaConversionImagenesSalida :
        return self.__estrategias[estrategia]

    def prepararSalida(self, img, estrategia: str):
        strg=self.leerEstrategia(estrategia)
        return strg.convertirSalida(img)
