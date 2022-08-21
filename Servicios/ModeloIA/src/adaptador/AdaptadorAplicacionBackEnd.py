import sys, os
import requests
sys.path.append(os.path.abspath(os.path.join('src/', 'configuraciones')))
from configuraciones import aplicacion_backEnd
import stomp
import sys
import time

class AdaptadorAplicatiovoBackEnd():

    def __init__(self, URL=aplicacion_backEnd["URL"]):
        self.URL = URL

    def obtenerImagen(self):
        return requests.get(self.URL)

#a = AdaptadorAplicatiovoBackEnd()

#print(a.obtenerImagen().json())




    