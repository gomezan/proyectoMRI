
from time import sleep
import requests
from dataclasses import dataclass

from integracion.back.AdaptadorBackInterfaz import AdaptadorBackInterfaz
from configuracion.AtributosConfiguracion import aplicacion_backEnd
#Cola
from integracion.back.cola.AdaptadorActiveMQInterfaz import  AdaptadorActiveMQInterfaz
from integracion.back.cola.AdaptadorActiveMQ import AdaptadorActiveMQ
#datos
from integracion.back.dto.CtrDtoInterfaz import CtrDtoInterfaz
from integracion.back.dto.CtrDto import CtrDto

@dataclass
class AdaptadorBack(AdaptadorBackInterfaz):

    #El back controla:
    # Adaptador de la cola hacia el back
    cola: AdaptadorActiveMQInterfaz = AdaptadorActiveMQ()
    # Dto del paquete con toda la información de la imagen
    dto: CtrDtoInterfaz = CtrDto()

    def __init__(self, URL=aplicacion_backEnd["URL"]):
        self.URL = URL

    def solicitarPaquete(self):
        banderaPaquete = False
        paquete = None
        while not banderaPaquete:
            try:
                paquete=requests.get(self.URL).json()
                if not 'status' in paquete :
                    banderaPaquete = True
                else:
                    sleep(3)
            except:
                sleep(3)
        #paquete={'imagenId': 8, 'nombre': 'prueba', 'observacion': 'datos adicionales', 'estado': 'PROCESANDO', 'descripcionOriginal': "", 'rutaOriginal': 'no_procesada/1.png', 'fechaInicial': '2022-01-16T00:48:21.102802', 'fechaEliminacion': '2022-01-19T00:48:21.102824', 'descripcionProcesada': None, 'rutaProcesada': 'procesado/1.png', 'fechaProcesamiento': '2022-02-06T02:04:43'}
        print(paquete)
        self.dto.almacenarPaquete(paquete)

    def obtenerImagen(self):
        return self.dto.solicitarURLImagen()

    def enviarCola(self, datos:{}):
        paquete=self.dto.crearPayload(datos)
        self.cola.enviarPayload(paquete)

    def desconectar(self):
        self.cola.desconectar()

    def actualizarPaquete(self, infoProcesada):
        self.dto.actualizarPaquete(infoProcesada)
        paquete=self.dto.getPaquete()
        self.cola.enviarPayload(paquete)
        self.dto.vaciarPaquete()