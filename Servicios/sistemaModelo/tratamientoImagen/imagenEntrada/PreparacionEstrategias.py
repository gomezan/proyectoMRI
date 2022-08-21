
from dataclasses import dataclass

from tratamientoImagen.imagenEntrada.procesamientoImagenes.EstrategiaProcesamientoImagenes import EstrategiaProcesamientoImagenes
from tratamientoImagen.imagenEntrada.conversionImagenes.EstrategiaConversionImagenesEntrada import EstrategiaConversionImagenesEntrada

# La responsabilidad de esta clase es contener una estrategia de procesemaiento de la imagen y una de conversión de forma que se manejan como una sola estrategia.

@dataclass
class PreparacionEstrategias():
    procesamiento: EstrategiaProcesamientoImagenes
    conversion: EstrategiaConversionImagenesEntrada