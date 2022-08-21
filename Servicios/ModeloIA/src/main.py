import requests
import json
from adaptador.AdaptadorActiveMQ import  AdaptadorActiveMQ
from adaptador.AdaptadorAplicacionBackEnd import AdaptadorAplicatiovoBackEnd
import datetime
import pytz



def main():
    adaptador = AdaptadorAplicatiovoBackEnd()
    adaptadorCola = AdaptadorActiveMQ()
    imagen =(adaptador.obtenerImagen().json())
    print(imagen)
    imagen["estado"] = "PROCESADO"
    imagen["rutaProcesada"] = "procesado/1.png"
    imagen["fechaProcesamiento"]= datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    imagen["descripcionProcesada"]= '{"algo":"pepe"}'
    print(json.dumps(imagen))
    adaptadorCola.enviarPayload( json.dumps(imagen))

    adaptadorCola.desconectar()

    

if __name__ == '__main__':
    main()
