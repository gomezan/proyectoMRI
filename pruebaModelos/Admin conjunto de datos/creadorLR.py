
import numpy as np
import os
import glob
import nibabel

# función de filtrado de imagen
def suavizar(img_stack, dim):
    # se guardan las dimensiones de la imagen
    x = img_stack.shape[0]
    y = img_stack.shape[1]
    z = img_stack.shape[2]
    # se crea la matriz en donde se guardara la nueva imagen
    img = np.zeros((x, y, z))
    # se recorre la imagen
    for i in range(x):
        for j in range(y):
            for k in range(z):
                # se calcula promedio
                prom = 0
                for l in range(dim):
                    for m in range(dim):
                        for n in range(dim):
                            prom += img_stack[max(i - l, 0)][max(j - m, 0)][max(k - n, 0)]
                # se guarda el promedio en la nueva imagen
                img[i][j][k] = int(prom / (dim ** 3))
                # img[i][j][k]=img_stack[i][j][k]
    a = 0
    for i in range(x):
        for j in range(y):
            for k in range(z):
                if img[i][j][k] > a:
                    a = img[i][j][k]
    print(a)
    return img

# función de sub.muestreo de imagen
def submuestreo(img_stack):

    x = img_stack.shape[0]
    y = img_stack.shape[1]
    z = img_stack.shape[2]
    # se crea la matriz en donde se guardara la nueva imagen
    img = np.zeros(( x//2 , y//2 , z//2))
    # se recorre la imagen
    for i in range(x):
        for j in range(y):
            for k in range(z):

                if not( i %2 | j% 2 | k % 2):
                    if((i// 2 !=x//2) and (j// 2 !=y//2) and (k// 2 !=z//2)):
                        img[i // 2][j // 2][k // 2] = img_stack[i][j][k]
    return img

# Se extraen todos los archivos .npy del folder de entrada.
files = sorted(glob.glob(r"C:\Users\Estudiante\Documents\datasetMRI\final\16x10k\parchesGT\*.npy"))

for filepath in files:
    # Se almacena la parte de la ruta que contiene el nombre de la imagen.
    aux = filepath.split(r"\u")
    name = aux[-1]
    print(name)
    # Se carga la imagen
    file = np.array(np.load(filepath), dtype = np.float32)
    print(file.shape)
    # Se realiza la decimación de la imagen
    resampled_img=  suavizar (file,2)
    resampled_img= submuestreo (resampled_img)
    # La imagen resultante se almacena en la ruta especificada
    resampled_img = np.array(resampled_img, dtype=np.float32)
    print(resampled_img.shape)
    np.save(r"C:\Users\Estudiante\Documents\datasetMRI\final\16x10k\parchesDecimados/Lsu"+name,resampled_img)

