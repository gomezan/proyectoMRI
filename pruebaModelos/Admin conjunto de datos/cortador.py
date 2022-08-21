
import numpy as np
import glob

# Función que elimina las esquinas 3d de un volumen.
def QuitarMarco(img):
    x = img.shape[0]
    y = img.shape[1]
    z = img.shape[2]
    img2 = np.zeros((x - 2, y - 2, z - 2))
    for i in range(x):
        for j in range(y):
            for k in range(z):
                if i < x - 1 and i > 0 and j < y - 1 and j > 0 and k < z - 1 and k > 0:
                    img2[i - 1][j - 1][k - 1] = img[i][j][k]

    return img2

# Se extraen todos los archivos .npy del folder de entrada.
files = sorted(glob.glob(r"C:\Users\Estudiante\Documents\datasetMRI\salvacion2.0\parchesLR\*.npy"))

for filepath in files:
    #Se almacena la parte de la ruta que contiene el nombre de la imagen.
    aux=filepath.split(r"\s")
    name=aux[-1]
    print(name)
    # Se carga la imagen
    file = np.array(np.load(filepath), dtype = np.float32)
    print(file.shape)
    # se remueven las esquinas de la imagen
    new_img= QuitarMarco(file)
    # Se almacena la imagen en la ruta especificada de salida
    new_img = np.array(new_img, dtype=np.float32)
    print(new_img.shape)
    np.save(r"C:\Users\Estudiante\Documents\datasetMRI\salvacion2.0\decCortados/s"+name,new_img)