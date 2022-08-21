#utils
from dataclasses import dataclass

from tratamientoImagen.FachadaProcesamientoInterfaz import FachadaProcesamientoInterfaz
from tratamientoImagen.imagenSalida.PosprocesamientoInterfaz import PosprocesamientoInterfaz
from tratamientoImagen.imagenSalida.Posprocesamiento import Posprocesamiento
from tratamientoImagen.imagenEntrada.PreprocesamientoInterfaz import PreprocesamientoInterfaz
from tratamientoImagen.imagenEntrada.Preprocesamiento import Preprocesamiento

@dataclass
class FachadaProcesamiento(FachadaProcesamientoInterfaz):

    #Contiene una clase dedicada al preprocesiamiento y otra al posprocesamiento
    salida: PosprocesamientoInterfaz = Posprocesamiento()
    entrada: PreprocesamientoInterfaz = Preprocesamiento()

    def prepararEntrada(self, img, estrategia: str):
        return self.entrada.prepararEntrada(img,estrategia)

    def prepararSalida(self, img, estrategia: str):
        return self.salida.prepararSalida(img,estrategia)