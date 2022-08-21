from tratamientoImagen.imagenEntrada.procesamientoImagenes.EstrategiaProcesamientoImagenes import EstrategiaProcesamientoImagenes
import math
import numpy as np

#Interpolación lanczos

L = {}
lx = {}
ly = {}

# Función SinC
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


# Filtro de lanczos
def Lanczos(img, x, y, z, a):
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

# Método de interpolación de Lanczos
def interpolacionLanczos3D(imgOriginal, a):
    xt, yt, zt = imgOriginal.shape
    y = []
    imgLanczos = np.zeros((xt * 2, yt * 2, zt * 2))
    for i in np.arange(0.0, xt - 0.5, 0.5):
        for j in np.arange(0.0, yt - 0.5, 0.5):
            for k in np.arange(0.0, zt - 0.5, 0.5):
                imgLanczos[int(i * 2), int(j * 2), int(k * 2)] = Lanczos(imgOriginal, i, j, k, a)
    return imgLanczos




class DCSRNlanczos(EstrategiaProcesamientoImagenes):

    def procesar(self, img):
        # Se utiliza el tamaño del filtro igual a 3.
        a=3
        # Interpolación Lanczos
        return interpolacionLanczos3D(img, a)