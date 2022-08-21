
from tratamientoImagen.imagenEntrada.conversionImagenes.EstrategiaConversionImagenesEntrada import EstrategiaConversionImagenesEntrada
from nibabel import  Nifti1Image

class NIFTIEntrada(EstrategiaConversionImagenesEntrada):

    def convertirEntrada(self, img):
        return Nifti1Image.from_bytes(img).get_data()
        
