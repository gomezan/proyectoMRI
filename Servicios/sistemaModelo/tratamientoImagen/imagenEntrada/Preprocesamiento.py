
from tratamientoImagen.imagenEntrada.PreprocesamientoInterfaz import PreprocesamientoInterfaz
from tratamientoImagen.imagenEntrada.PreparacionEstrategiasFactory import PreparacionEstrategiasFactory
from tratamientoImagen.imagenEntrada.PreparacionEstrategias import PreparacionEstrategias

from tratamientoImagen.imagenEntrada.conversionImagenes.NIFTIEntrada import NIFTIEntrada
from tratamientoImagen.imagenEntrada.conversionImagenes.DICOMEntrada import DICOMEntrada
from tratamientoImagen.imagenEntrada.procesamientoImagenes.DCSRNlanczos import DCSRNlanczos
from tratamientoImagen.imagenEntrada.procesamientoImagenes.DCSRNnn import DCSRNnn

class Preprocesamiento(PreprocesamientoInterfaz):

    # Diccionario que relaciona el string con la estrategia de pre-procesmaiento
    def __init__(self):
        self.__factories={
           "DCSRNLanczos_NIFTI": PreparacionEstrategiasFactory(DCSRNlanczos, NIFTIEntrada),
           "DCSRNnn_NIFTI": PreparacionEstrategiasFactory(DCSRNnn, NIFTIEntrada),

        }

    # Función encargada de instanciar una factoria especifica dada la estrategia
    def leerFactoria(self, estrategia: str) -> PreparacionEstrategiasFactory :
        return self.__factories[estrategia]

    # Función encargada de realizar la conversión a numpy y preparar la imagen para la red.
    def modificacionImagen(self, encargadoImagen: PreparacionEstrategias, img ):
        imgFinal = encargadoImagen.conversion.convertirEntrada(img)
        imgFinal=encargadoImagen.procesamiento.procesar(imgFinal)
        return imgFinal

    def prepararEntrada(self, img, estrategia: str):
        factory= self.leerFactoria(estrategia)
        encargado=factory()
        return self.modificacionImagen(encargado,img)