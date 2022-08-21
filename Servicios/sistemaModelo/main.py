
#modelos de red neuronal
from modelo.DCSRN import DCSRN

#interfaces de integracion
from integracion.FachadaIntegracion import FachadaIntegracion

#Procesamiento de imágenes
from tratamientoImagen.FachadaProcesamiento import FachadaProcesamiento

#controlador
from controlador.ControladorIA import ControladorIA

from datetime import datetime

#librerias utiles
import matplotlib.pyplot as plt
from datetime import datetime



#Función encargada de obtener la parte de la ruta que contiene el nombre de la imagen
def generadorNombres(name: str):
    nombre=url.replace('s3://imagenes-tesis/','').split("/")
    return "procesada/"+nombre[1]


print("Starting....")    
print(datetime.now())


if __name__ == '__main__':

    #Parametros
    estrategiaEnt="DCSRNLanczos_NIFTI"
    estrategiaSal = "NIFTI"

    #Creación del controlador
    ctr=ControladorIA(DCSRN(), FachadaProcesamiento(), FachadaIntegracion())

    #EJECUCION CODIGO

    while True:
        # 1. Se pide información de la imagen al back
        print("Solicitando imagen a procesar....")    
        ctr.solicitarPaquete()
        # Se pide la llave S3 de dicha imagen
        url = ctr.solicitarImagen()
        print("url a procesar: ", url)        

        #2. Se solicita la imagen al sistemaArchivos s3

        print("obteniendo imagen....")    
        print(datetime.now())
        img=ctr.buscarImagen(url.replace('s3://imagenes-tesis/',''))
        if not img:
            ctr.actualizarPaquete({"estado":"NO_ENCONTRADO","descripcionProcesada":"{}","rutaProcesada": 's3://imagenes-tesis/',"fechaProcesamiento": datetime.now().strftime("%Y-%m-%d %H:%M:%S") })
        else:
            print("obtuve la imagen....")    
            print(datetime.now())
            print(type(img))
            

            print("procesando imagen....")    
            print(datetime.now())
            #3. Se prepara la imagen para la red
            img = ctr.procesarImagenEntrada(img, estrategiaEnt)
            print("Imagen procesada....")    
            print(datetime.now())
            #print(type(img))
            #print(img.shape)

            print("prediciendo imagen....")    
            print(datetime.now())
            #4. La red procesa la imagen de entrada
            predicted = ctr.predecirImagen(img)
            print("imagen predecida....")    
            print(datetime.now())
            #print(type(predicted))
            #print(predicted.shape)

            print("procesando imagen salida....")    
            print(datetime.now())
            #5. Se procesa la imagen al formato deseado y se almacena
            imgFinal = ctr.procesarImagenSalida(predicted, estrategiaSal)
            print("imagen salida procesada....")    
            print(datetime.now())

            print("subiendo imagen....")    
            print(datetime.now())
            nuevoURL=generadorNombres(url)
            #6. Se carga la imagen al sistema de archivos s3
            ctr.cargarImagen(imgFinal,nuevoURL)

            print("imagen subida....")    
            print(datetime.now())
            # 7. Se actualiza el paquete con la información modificada de la imagen.
            ctr.actualizarPaquete({"estado":"PROCESADO","descripcionProcesada":"{}","rutaProcesada": 's3://imagenes-tesis/'+nuevoURL,"fechaProcesamiento": datetime.now().strftime("%Y-%m-%d %H:%M:%S") })



