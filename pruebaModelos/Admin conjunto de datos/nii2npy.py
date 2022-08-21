import numpy as np
import os
import glob
import nibabel

outdir = '../HCP_NPY'
if not os.path.exists(outdir):
    os.makedirs(outdir)

# Se extraen todos los archivos .nii del folder de entrada.
files = glob.glob(r"C:\Users\Estudiante\Documents\datasetMRI\salvacion\groundTruthNII\*.nii")
for filepath in files:
    # Se almacena la parte de la ruta que contiene el nombre de la imagen.
    aux = filepath.split()
    name = aux[-1]
    print(name)
    # Se carga la imagen a procesar y se almacena el numpy de esta
    file = nibabel.load(filepath).get_data().transpose(1, 0, 2)
    print('  Data shape is ' + str(file.shape) + ' .')
    # Se almacena el numpy array previamnete obtenido
    filename_ = filepath.split('/')[-1].split('.')[0]
    filename = filename_ + '.npy'
    file1 = os.path.join(outdir, filename)
    np.save(file1, file)
    print('File ' + filename_ + ' is saved in ' + file1 + ' .')

