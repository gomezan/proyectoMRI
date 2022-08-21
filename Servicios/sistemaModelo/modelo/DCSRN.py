from os.path import abspath, join
import tensorflow as tf
from modelo.RedNeuronal import RedNeuronal
from modelo.model import Generator
import numpy as np

class DCSRN(RedNeuronal):

    def __init__(self):
        #Ubicación de los pesos del entrenamiento
        path = r"/Users/saropi/Documents/universidad/tesis/Servicios/sistemaModelo/modelo/pesos"
        # Definición del tamaño del parche
        self.__PATCH_SIZE=30
        #Creación del modelo
        self.__generator_g = Generator(self.__PATCH_SIZE)
        ckpt = tf.train.Checkpoint(generator_g=self.__generator_g)
        ckpt_manager = tf.train.CheckpointManager(ckpt, path, max_to_keep=3)
        ckpt.restore(ckpt_manager.latest_checkpoint)

    # Función encargada de realizar la super resolución sobre un único parche
    def predictor(self, img):
        x = np.reshape(img, (self.__PATCH_SIZE, self.__PATCH_SIZE, self.__PATCH_SIZE, 1))
        prediction = self.__generator_g(x, training=False).numpy()
        return np.reshape(prediction, (self.__PATCH_SIZE, self.__PATCH_SIZE, self.__PATCH_SIZE))

    # Función encargada de realizar la super resolución sobre la totalidad de la imagen
    def predecirImagen(self, img_stack):
        tam=self.__PATCH_SIZE
        x = img_stack.shape[0]
        y = img_stack.shape[1]
        z = img_stack.shape[2]
        img = np.zeros((x, y, z))
        count = np.zeros((x, y, z))
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
                    img2 = self.predictor(img2)
                    for l in range(a, a + tam):
                        for m in range(b, b + tam):
                            for n in range(c, c + tam):
                                if img[l][m][n]:
                                    if not (
                                            l == a or l == a + tam - 1 or m == b or m == b + tam - 1 or n == c or n == c + tam - 1):

                                        img[l][m][n] = max(img2[l - a][m - b][n - c], img[l][m][n])
                                else:
                                    if not (
                                            l == a or l == a + tam - 1 or m == b or m == b + tam - 1 or n == c or n == c + tam - 1):
                                        img[l][m][n] = img2[l - a][m - b][n - c]



        return img





