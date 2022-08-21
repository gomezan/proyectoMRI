

from tratamientoImagen.imagenSalida.EstrategiaConversionImagenesSalida import EstrategiaConversionImagenesSalida
from nibabel import  Nifti1Image
from numpy import eye

class NIFTISalida(EstrategiaConversionImagenesSalida):

    def convertirSalida(self, img):
        return Nifti1Image(img, eye(4)).to_bytes()
