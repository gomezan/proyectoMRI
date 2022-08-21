

import numpy as np
import os
import glob
import math

L = {}
lx = {}
ly = {}

# Función Sinc
def sinc(x):
    if x:
        return (math.sin(x * math.pi) / (x * math.pi))
    else:
        return (1.0)

def l(x, a):
    if x < a and x > -a:
        return (sinc(x) * sinc(x / a))
    else:
        return (0)


# Filtro Lanczos
def Lanczos_Interpolation(img, x, y, z, a):
    xt, yt, zt = img.shape
    xi = max(math.floor(x) - a + 1, 0)
    xf = min(math.floor(x) + a, xt)
    yi = max(math.floor(y) - a + 1, 0)
    yf = min(math.floor(y) + a, yt)
    zi = max(math.floor(z) - a + 1, 0)
    zf = min(math.floor(z) + a, zt)
    size = 2 * a - 1
    tempx = np.zeros((size, size))
    tempy = np.zeros((size))
    m = 0
    for k in range(zi, zf):
        n = 0
        for j in range(yi, yf):
            for i in range(xi, xf):
                if not (x - i, a) in L:
                    L[(x - i, a)] = l(x - i, a)
                tempx[m][n] += img[i, j, k] * L[(x - i, a)]
            n += 1
        m += 1
    m = 0
    for k in range(zi, zf):
        n = 0
        for j in range(yi, yf):
            if not (y - j, a) in L:
                L[(y - j, a)] = l(y - j, a)
            tempy[m] += tempx[m][n] * L[(y - j, a)]
            n += 1
        m += 1
    m = 0
    value = 0
    for k in range(zi, zf):
        if not (z - k, a) in L:
            L[(z - k, a)] = l(z - k, a)
        value += tempy[m] * L[(z - k, a)]
        m += 1
    return value

def KNN(img,x,y,z):
    return img[int(x),int(y),int(z)]

#Método de interpolación vecinos más cercanos
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

#Método de interpolación de Lanczos
def interpolacionLanczos3D(imgOriginal, a):
    xt, yt, zt = imgOriginal.shape
    y = []
    imgLanczos = np.zeros((xt * 2, yt * 2, zt * 2))
    for i in np.arange(0.0, xt , 0.5):
        for j in np.arange(0.0, yt , 0.5):
            for k in np.arange(0.0, zt , 0.5):
                imgLanczos[int(i * 2), int(j * 2), int(k * 2)] = Lanczos_Interpolation(imgOriginal, i, j, k, a)
    return imgLanczos

# Se extraen todos los archivos .npy del folder de entrada.
files = sorted(glob.glob(r"C:\Users\Estudiante\Documents\datasetMRI\final\16x10k\parchesDecimados\*.npy"))


for filepath in files:
    # Se almacena la parte de la ruta que contiene el nombre de la imagen.
    aux = filepath.split(r"\L")
    name = aux[-1]
    print(name)
    # Se carga la imagen
    file = np.array(np.load(filepath), dtype = np.float32)
    # Se realiza el proceso de interpolación
    #resampled_img= interpolacionVecinos(file)
    resampled_img=interpolacionLanczos3D(file, 4)
    # Se almacena la imagen en la ruta especificada
    resampled_img = np.array(resampled_img, dtype=np.float32)
    print(resampled_img.shape)
    np.save(r"C:\Users\Estudiante\Documents\datasetMRI\final\16x10k\parchesExpandidos\N"+name,resampled_img)