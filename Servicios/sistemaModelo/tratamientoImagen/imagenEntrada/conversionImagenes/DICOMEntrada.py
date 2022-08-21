
#utils
import cv2
from keras.preprocessing.image import img_to_array

from tratamientoImagen.imagenEntrada.conversionImagenes.EstrategiaConversionImagenesEntrada import EstrategiaConversionImagenesEntrada


class DICOMEntrada(EstrategiaConversionImagenesEntrada):

    def __init__(self):
        self.__SIZE=256

    def convertirEntrada(self, img):
        #print("funciona DICOM")
        imagen = cv2.resize(img, (self.__SIZE, self.__SIZE))
        imagen = imagen.astype('float32') / 255.0
        arreglo = img_to_array(imagen)
        return arreglo
