
import tensorflow as tf
from DCSRNomagdy.DCSRNmain.model import Generator
import numpy as np
import nibabel.processing
from os.path import abspath


def identidad(img):
    x = img.shape[0]
    y = img.shape[1]
    z = img.shape[2]
    img2= np.zeros((x,y,z))
    for i in range(x):
        for j in range(y):
            for k in range(z):
                img2[i][j][k]=img[i][j][k]
    return img2

def predictor(img, PATCH_SIZE):
    x=np.reshape(img, (PATCH_SIZE,PATCH_SIZE,PATCH_SIZE,1))
    path=r"C:\Users\Estudiante\Documents\datasetMRI\pesos"
    generator_g = Generator(PATCH_SIZE)
    ckpt = tf.train.Checkpoint(generator_g=generator_g)
    ckpt_manager = tf.train.CheckpointManager(ckpt, path, max_to_keep=3)
    ckpt.restore(ckpt_manager.latest_checkpoint)
    prediction = generator_g(x, training=False).numpy()
    return np.reshape(prediction, (PATCH_SIZE,PATCH_SIZE,PATCH_SIZE))


def SR(img_stack, tam):
    x = img_stack.shape[0]
    y = img_stack.shape[1]
    z = img_stack.shape[2]
    img = np.zeros((x, y, z))
    for i in range(0, x, tam // 2):
        for j in range(0, y, tam // 2):
            for k in range(0, z, tam // 2):
                a = i
                b = j
                c = k
                if i + tam >= x:
                    a = x - tam
                if j + tam >= y:
                    b = y - tam
                if k + tam >= z:
                    c = z - tam

                img2 = np.zeros((tam, tam, tam))

                for l in range(a, a + tam):
                    for m in range(b, b + tam):
                        for n in range(c, c + tam):
                            img2[l - a][m - b][n - c] = img_stack[l][m][n]

                img2 = predictor(img2,tam)

                for l in range(a, a + tam):
                    for m in range(b, b + tam):
                        for n in range(c, c + tam):
                            if img[l][m][n]:
                                img[l][m][n] = (img2[l - a][m - b][n - c] + img[l][m][n]) // 2
                            else:
                                img[l][m][n] = img2[l - a][m - b][n - c]

    return img

#leer imagen
input_path = abspath(r"C:\Users\Estudiante\Documents\datasetMRI\pruebas\datsetPruebas\KNN\KNN_1.nii")
output_path = abspath(r"C:\Users\Estudiante\Documents\datasetMRI\pruebas\datsetPruebas\modelo\SR_1.nii")


input_img = nibabel.load(input_path)
imgOriginal = np.array(input_img.dataobj, dtype=np.int32)


print("original: ",imgOriginal.shape )

resampled_img= SR(imgOriginal,16)

resampled_img = np.array(resampled_img, dtype=np.int32)

#imprimir dimensiones imagen output
print("resultado: ",resampled_img.shape )

#guardar imagen
new_image = nibabel.Nifti1Image(resampled_img, affine=input_img.affine)
nibabel.save(new_image, output_path)


