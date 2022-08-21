
import numpy as np
import os
import glob

#Directorios de salida para almacenar el ground truth y las imagenes decimadas respectivamente.
outdirGT = r'C:\Users\Estudiante\Documents\datasetMRI\salvacion2.0\parchesHR'
outdirComp = r'C:\Users\Estudiante\Documents\datasetMRI\salvacion2.0\parchesLR'
if not os.path.exists(outdirGT):
    os.makedirs(outdirGT)
if not os.path.exists(outdirComp):
    os.makedirs(outdirComp)

# Se extraen todos los archivos .npy del folder del ground truth y las imágenes decimadas respectivamente.
GT = sorted(glob.glob(r"C:\Users\Estudiante\Documents\datasetMRI\salvacion\groundTruthNPY\*.npy"))
comp=sorted(glob.glob(r"C:\Users\Estudiante\Documents\datasetMRI\salvacion\decimadasExpandidasNPY\*.npy"))

for filepathGT, filepathComp in zip (GT, comp):
    #Se cargan las imagenes
    fileGT = np.array(np.load(filepathGT), dtype = np.float32)
    fileComp = np.array(np.load(filepathComp), dtype=np.float32)
    print('  Data shape of GT ' + str(fileGT.shape) + ' .')
    print('  Data shape of Comp ' + str(fileComp.shape) + ' .')
    # El contador contiene la cantidad de pares parches obtenidos
    cont=0
    while (cont < 500):
        # Se obtienen posiciones de forma aleatoria en los 3 ejes sobre la imagen decimada.
        x = int(np.floor((fileComp.shape[0] - 32) * np.random.rand(1))[0])
        y = int(np.floor((fileComp.shape[1] - 32) * np.random.rand(1))[0])
        z = int(np.floor((fileComp.shape[2] - 32) * np.random.rand(1))[0])
        # Se recorta el parche de las posiciones obtenidas anteriormente.
        file_augComp = fileComp[x:x + 32, y:y + 32, z:z + 32]

        # Se obtiene el promedio del parche previamente obtenido para filtrar parches vacios.
        prom = np.mean(file_augComp)

        # Solo si el parche previamnete obtenido es mayor a 70 se procede a ser almacenado
        if( 70 < prom ):
            # Se carga el parche homologo en las mismas dimensiones sobre el ground truth
            file_augGT = fileGT[x:x + 32, y:y + 32, z:z + 32]

            # Se almacena el parche del gropund truth
            filename_GT = filepathGT.split(r"\--")[-1].split('.')[0]
            filename_GT = filename_GT + '_' + str(cont) + '.npy'
            filename = os.path.join(outdirGT, filename_GT)
            print(filename)
            np.save(filename, file_augGT)

            # Se almacena el parche de la imagen decimada
            filename_Comp = filepathComp.split(r"\HR--")[-1].split('.')[0]
            filename_Comp = filename_Comp + '_' + str(cont) + '.npy'
            filename = os.path.join(outdirComp, filename_Comp)
            print(filename)
            np.save(filename, file_augComp)

            # Se cuenta los parches recientemente creados.
            cont = cont + 1

    print('All sliced files of ' + filepathGT + ' are saved.')
    print('All sliced files of ' + filepathComp + ' are saved.')