from tratamientoImagen.imagenEntrada.procesamientoImagenes.EstrategiaProcesamientoImagenes import EstrategiaProcesamientoImagenes
import math
import numpy as np


#Interpolación vecino más cercano

def KNN(img,x,y,z):
    return img[int(x),int(y),int(z)]

def interpolacionVecinos(img):

    imgOriginal = img
    print("original: ",imgOriginal.shape )
    y=[]
    tamx=img.shape[0]
    tamy= img.shape[1]
    tamz= img.shape[2]

    imgKNN=np.zeros((tamx*2,tamy*2,tamz*2))
    for i in np.arange(0.0, tamx, 0.5):
        for j in np.arange(0.0, tamy, 0.5):
            for k in np.arange(0.0, tamz, 0.5):
                imgKNN[int(i*2),int(j*2),int(k*2)]=KNN(imgOriginal,i,j,k)
    return(imgKNN)


class DCSRNnn(EstrategiaProcesamientoImagenes):

    def procesar(self, img):
        return interpolacionVecinos(img)