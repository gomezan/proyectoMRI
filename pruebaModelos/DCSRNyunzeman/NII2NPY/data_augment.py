import numpy as np
import os
import glob

outdir = r'C:\Users\Estudiante\Documents\datasetMRI\final\16x10k\parchesGT'
if not os.path.exists(outdir):
    os.makedirs(outdir)

files = glob.glob(r"C:\Users\Estudiante\Documents\datasetMRI\final\numpies\*.npy")
for filepath in files:
    file = np.array(np.load(filepath), dtype = np.float32)
    print('  Data shape is ' + str(file.shape) + ' .')
    cont=0
    while (cont < 10000):
        x = int(np.floor((file.shape[0] - 16) * np.random.rand(1))[0])
        y = int(np.floor((file.shape[1] - 16) * np.random.rand(1))[0])
        z = int(np.floor((file.shape[2] - 16) * np.random.rand(1))[0])
        file_aug = file[x:x + 16, y:y + 16, z:z + 16]

        prom = np.mean(file_aug)

        if( 50 < prom ):
            filename_ = filepath.split(r"\s")[-1].split('.')[0]
            filename_ = filename_ + '_' + str(cont) + '.npy'
            filename = os.path.join(outdir, filename_)
            print(filename)
            np.save(filename, file_aug)
            cont=cont+1

    print('All sliced files of ' + filepath + ' are saved.')