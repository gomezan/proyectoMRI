

import glob
import numpy as np
import nibabel
import math
import napari
import tensorflow as tf

# Función genera un volumen con valores aleatorios
def volumenAleatorio(tam):
  return np.random.choice(range(256),(tam,tam, tam))

# Genera un volumen con el patrón de un tablero de ajedrez
def volumenAjedrez(tam):
  ajd=np.zeros((tam,tam,tam), dtype=np.uint8)
  ajd[1::2, ::2] = 1
  ajd[::2, 1::2] = 1
  ajd=ajd*255
  return ajd

# Función que calcula el error cuadratico medio de dos imagenes.
def mse(img1,img2):
    sum = 0
    x, y, z = img1.shape
    for i in range(x):
        for j in range(y):
            for k in range(z):
                sum += (img1[i, j, k] - img2[i, j, k]) **2
    return  sum / (x * y * z)

# Función que calcula el PSNR de dos imágenes.
# Se debe especificar el número de bits que representan el valor de mayor tamaño de la imagen.
def psnr(A,B, bits):
    x=20*math.log10((2**bits)-1)
    y = 10 * math.log10(mse(A,B))
    return x-y

# Función encargada de igualar el tamaño de dos imágenes con el objetivo que sean comparables.
def igualador(gt, comp):
    x1,y1,z1=gt.shape
    x2, y2, z2 = comp.shape
    newGt=gt[0:min(x1,x2),0:min(y1,y2),0:min(z1,z2)]
    newComp=comp[0:min(x1,x2),0:min(y1,y2),0:min(z1,z2)]
    return newGt, newComp

# Diccionario que relaciona las imágenes a probar con las rutas de ubicación de estos.
rutas={'GT': r"C:\Users\Estudiante\Documents\datasetMRI\final\soloEval\nifti\*.nii",
'NN': r"C:\Users\Estudiante\Documents\datasetMRI\final\pruebas\NN\*.nii",
'lan3': r"C:\Users\Estudiante\Documents\datasetMRI\pruebas\datsetPruebas\Lanczos3\*.nii",
'lan4': r"C:\Users\Estudiante\Documents\datasetMRI\pruebas\datsetPruebas\Lanczos4\*.nii",
       # Estas son diferentes imagenes provenientes de pesos del modelo
'salv1': r"C:\Users\Estudiante\Documents\datasetMRI\pruebas\datsetPruebas\modeloSalvacion1\*.nii",
'salv2': r"C:\Users\Estudiante\Documents\datasetMRI\pruebas\datsetPruebas\modeloSalvacion2\*.nii",
'salv3': r"C:\Users\Estudiante\Documents\datasetMRI\pruebas\datsetPruebas\modeloSalvacion3\*.nii",
'salv4': r"C:\Users\Estudiante\Documents\datasetMRI\pruebas\datsetPruebas\modeloSalvacion4\*.nii",
'salv6': r"C:\Users\Estudiante\Documents\datasetMRI\pruebas\datsetPruebas\modeloSalvacion6\*.nii",
'salv7': r"C:\Users\Estudiante\Documents\datasetMRI\pruebas\datsetPruebas\modeloSalvacion7\*.nii",
'salv8': r"C:\Users\Estudiante\Documents\datasetMRI\pruebas\datsetPruebas\modeloSalvacion8\*.nii",
'salv9': r"C:\Users\Estudiante\Documents\datasetMRI\pruebas\datsetPruebas\modeloSalvacion9\*.nii",
'salv10': r"C:\Users\Estudiante\Documents\datasetMRI\pruebas\datsetPruebas\modeloSalvacion10\*.nii",
'seg6': r"C:\Users\Estudiante\Documents\datasetMRI\pruebas\datsetPruebas\modeloSeguro6\*.nii",
'seg4': r"C:\Users\Estudiante\Documents\datasetMRI\pruebas\datsetPruebas\modeloSeguro4\*.nii",
'fin6': r"C:\Users\Estudiante\Documents\datasetMRI\pruebas\datsetPruebas\modeloApuestaFinal6\*.nii",
'fin3': r"C:\Users\Estudiante\Documents\datasetMRI\pruebas\datsetPruebas\modeloApuestaFinal3\*.nii"
}

# Diccionario que relaciona el método a utilizar con el nombre del array que contiene el psnr de dicho metodo.
psnrDic={
'NN': '\psnrNN.npy',   # Vecinos mas cercanos
'lan3': '\psnrLan3.npy',   # lanczos 3
'lan4': '\psnrLan4.npy',  # lanczos 4
    # Estos son diferentes psnr provenientes de pesos del modelo
'salv1': '\psnrSalv1.npy',
'salv2': '\psnrSalv2.npy',
'salv3': '\psnrSalv3.npy',
'salv4': '\psnrSalv4.npy',
'salv6': '\psnrSalv6.npy',
'salv7': '\psnrSalv7.npy',
'salv8': '\psnrSalv8.npy',
'salv9': '\psnrSalv9.npy',
'salv10': '\psnrSalv10.npy',
'seg6': '\psnrSeg6.npy',
'seg4': '\psnrSeg4.npy',
'fin6': '\psnrFin.npy',
'fin3': '\psnrFin3.npy'
}

# Diccionario que relaciona el método a utilizar con el nombre del array que contiene el ssim de dicho metodo.
ssimDic={
'NN': '\ssimNN.npy',   # vecinos mas cercanos
'lan3': '\ssimLan3.npy',  # lanczos 3
'lan4': '\ssimLan4.npy',   # lanczos 4
    # Estos son diferentes ssim provenientes de pesos del modelo
'salv1': '\ssimSalv1.npy',
'salv2': '\ssimSalv2.npy',
'salv3': '\ssimSalv3.npy',
'salv4': '\ssimSalv4.npy',
'salv6': '\ssimSalv6.npy',
'salv7': '\ssimSalv7.npy',
'salv8': '\ssimSalv8.npy',
'salv9': '\ssimSalv9.npy',
'salv10': '\ssimSalv10.npy',
'seg6': '\ssimSeg6.npy',
'seg4': '\ssimSeg4.npy',
'fin6': '\ssimFin.npy',
'fin3': '\ssimFin3.npy'
}
# Estas variables controlan si se deben correr las funciones del PSNR y SSIM sobre las imagenes.
#En caso de encontrase en falso, no se corren las fuinciones y se cragan los resultados directamente.
correrPSNR= False
correrSSIM= False
# Método a evaluar
metodo='salv8'
# Número de bits utilizados en el psnr
bits=13

# Se carga la ubicación del metodo a comparar
comparativa=rutas[metodo]

# Siempre se cargan las imágenes del ground truth ya que es el referente de resolución
filesGt = sorted(glob.glob(rutas['GT']))
# Se cargan las imágenes del metodo a comparar
filesComp=sorted(glob.glob(comparativa))

print(filesComp)


if(correrPSNR):

    # En esta se almacenan los resultados del PSNR
    res=[]
    for i,j in zip(filesGt, filesComp):
        # Se cargan ambas imagenes
        gt=nibabel.load(i).get_fdata()
        comp= nibabel.load(j).get_fdata()
        print(i)
        print(gt.shape)
        print(np.max(gt))
        print(j)
        print(comp.shape)
        print(np.max(comp))
        # Si las imagenes tienen dimensiones iguales se obtiene el PSNR y se almacena
        if(np.array_equal(gt.shape, comp.shape)):
            res.append(psnr(gt,comp, bits))
        # Si las imagenes no tienen dimensiones iguales
        # se igualan las dimesniones, se obtiene el PSNR y se almacena
        else:
            gt, comp = igualador(gt, comp)
            res.append(psnr(gt, comp, bits))

    # Se almacenan los resultados en la carpeta especificada
    array=np.array(res)
    print(array)
    np.save(r"C:\Users\Estudiante\Documents\datasetMRI\final\pruebas\resultados"+psnrDic[metodo],array)

if(correrSSIM):

    # En esta se almacenan los resultados del PSNR
    res=[]
    for i,j in zip(filesGt, filesComp):
        # Se cargan ambas imagenes
        gt=nibabel.load(i).get_fdata()
        comp= nibabel.load(j).get_fdata()
        print(i)
        print(gt.shape)
        mayor = np.max(gt)
        print(mayor)
        print(j)
        print(comp.shape)
        print(np.max(comp))
        # Si las imagenes tienen dimensiones iguales se obtiene el ssiM y se almacena
        if(np.array_equal(gt.shape, comp.shape)):
            aux = tf.image.ssim(gt, comp, max_val=mayor, filter_size=11,
                                filter_sigma=1.5, k1=0.01, k2=0.03)
            res.append(float(aux))
        # Si las imagenes no tienen dimensiones iguales
        # se igualan las dimesniones, se obtiene el SSIM y se almacena
        else:
            gt, comp= igualador(gt,comp)
            aux = tf.image.ssim(gt, comp, max_val=mayor, filter_size=11,
                                filter_sigma=1.5, k1=0.01, k2=0.03)
            res.append(float(aux))

    # Se almacenan los resultados en la carpeta especificada
    array=np.array(res)
    print(array)
    np.save(r"C:\Users\Estudiante\Documents\datasetMRI\final\pruebas\resultados"+ssimDic[metodo],array)

# Se cargan los resultados del psnr y el ssim
psnrRes=np.load(r"C:\Users\Estudiante\Documents\datasetMRI\final\pruebas\resultados"+psnrDic[metodo])
ssimRes=np.load(r"C:\Users\Estudiante\Documents\datasetMRI\final\pruebas\resultados"+ssimDic[metodo])

# Se imprimen estiligrafos asociados a los resultados
print("************** PSNR **********")
print("promedio ", psnrRes.mean())
print("std ", np.std(psnrRes))
print("mediana ", np.median(psnrRes))
print("minimo ", np.amin(psnrRes))
print("maximo ", np.amax(psnrRes))
print("***")
print("************** SSIM **************** ")
print("promedio ", ssimRes.mean())
print("std ", np.std(ssimRes))
print("mediana ", np.median(ssimRes))
print("minimo ", np.amin(ssimRes))
print("maximo ",  np.amax(ssimRes))
print("***")



#viewer = napari.Viewer(ndisplay=3)
#layer = viewer.add_image(np.load(r"C:\Users\Estudiante\Documents\datasetMRI\final\pruebas\NN\Nsub-MA232_run-1_T1w.NPY"))
#napari.run()
