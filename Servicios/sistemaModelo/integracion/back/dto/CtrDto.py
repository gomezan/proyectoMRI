

from integracion.back.dto.CtrDtoInterfaz import CtrDtoInterfaz
from integracion.back.dto.ImagenDto import ImagenDto

class CtrDto(CtrDtoInterfaz):


    def __init__(self):
        # Para disminuir el acoplamiento en el controlador el paquete se almacena en esta clase
        #encargada de gestionar todo lo relacionado con el dto.
        self.__paquete=None

    def almacenarPaquete(self, paquete):
        self.__paquete=ImagenDto(paquete)


    def actualizarPaquete(self, infoProcesada):
        DescipcionProcesada=infoProcesada["descripcionProcesada"]
        RutaProcesada = infoProcesada["rutaProcesada"]
        FechaProcesamiento=infoProcesada["fechaProcesamiento"]
        Estado=infoProcesada["estado"]
        self.__paquete.setDescipcionProcesada(DescipcionProcesada)
        self.__paquete.setRutaProcesada(RutaProcesada)
        self.__paquete.setFechaProcesamiento(FechaProcesamiento)
        self.__paquete.setEstado(Estado)

    def solicitarURLImagen(self):
        return self.__paquete.getRutaOriginal()

    def getPaquete(self):
        return self.__paquete

    def vaciarPaquete(self):
        self.__paquete = None



