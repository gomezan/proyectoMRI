import sys, os
sys.path.append(os.path.abspath(os.path.join('src/', 'configuraciones')))
from configuraciones import activeMQ
import stomp
import sys
import time

class AdaptadorActiveMQ():

    conexion = stomp.Connection(host_and_ports=[(activeMQ["URL"] , activeMQ["PORT"])], prefer_localhost=False) 
    
    def __init__(self):
        pass
    
    def enviarPayload(self, payload):
        AdaptadorActiveMQ.conexion.connect(activeMQ["USUARIO"], activeMQ["CLAVE"], wait=True)
        AdaptadorActiveMQ.conexion.send(body=payload, destination=activeMQ["RUTA"])
    
    def desconectar(self):
        AdaptadorActiveMQ.conexion.disconnect()
#adaptador = AdaptadorActiveMQ()
#adaptador.enviarPayload('{"msj":"hola"}')
#adaptador.desconectar()
