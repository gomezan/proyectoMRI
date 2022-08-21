
from integracion.back.cola.AdaptadorActiveMQInterfaz import AdaptadorActiveMQInterfaz
from configuracion.AtributosConfiguracion import activeMQ
import stomp
import sys
import time
from json import dumps

class AdaptadorActiveMQ(AdaptadorActiveMQInterfaz):

    conexion = stomp.Connection(host_and_ports=[(activeMQ["URL"] , activeMQ["PORT"])], prefer_localhost=False)

    def __init__(self):
        pass

    def enviarPayload(self, payload):
        AdaptadorActiveMQ.conexion.connect(activeMQ["USUARIO"], activeMQ["CLAVE"], wait=True)
        print("*********")
        print(payload.__dict__)
        print("*********")
        AdaptadorActiveMQ.conexion.send(body=dumps(payload.__dict__), destination=activeMQ["RUTA"])

    def desconectar(self):
        AdaptadorActiveMQ.conexion.disconnect()