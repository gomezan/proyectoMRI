

from dataclasses import dataclass

from tratamientoImagen.imagenEntrada.procesamientoImagenes.EstrategiaProcesamientoImagenes import EstrategiaProcesamientoImagenes
from tratamientoImagen.imagenEntrada.conversionImagenes.EstrategiaConversionImagenesEntrada import EstrategiaConversionImagenesEntrada
from tratamientoImagen.imagenEntrada.PreparacionEstrategias import PreparacionEstrategias

@dataclass
class PreparacionEstrategiasFactory():

    claseProcesamiento: type[EstrategiaProcesamientoImagenes]
    claseConversion: type[EstrategiaConversionImagenesEntrada]

    # Bajo el método call se instancian las clase destinadas a la conversión y procesamiento de imágenes.
    def __call__(self) -> PreparacionEstrategias:
        return PreparacionEstrategias(
            self.claseProcesamiento(),
            self.claseConversion()
        )