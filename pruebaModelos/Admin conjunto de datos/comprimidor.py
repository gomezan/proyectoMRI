
import numpy as np
import os
import glob

# Se extraen todos los archivos .npy del folder de entrada.
files = sorted(glob.glob(r"C:\Users\Estudiante\Documents\datasetMRI\salvacion2.0\gtCortados\*.npy"))
# Se crea una lista donde se almacenan los parches.
comp=[]
print(len(files))
for filepath in files:
    file = np.array(np.load(filepath), dtype = np.float32)
    comp.append(file)
    print(filepath)
    print(file.shape)

# Una vez todos los parches se encuentran almacenados se crea un array a partir de la lista.
res=np.array(comp)
# Se adiciona una dimensión al archivo de salida.
# La forma del array final debe ser (# parches, tam_parche, tam_parche, tam_parche, 1)
res=np.reshape(res,(8500,30,30,30,1))
print(res.shape)
#Alamacena el array con el nombre especificado.
np.save("3d_hr_data.npy",res)