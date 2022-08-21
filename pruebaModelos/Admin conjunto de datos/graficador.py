

import numpy as np
import seaborn
import pandas as pd
import matplotlib.pyplot as plt

#Permite relacionar el método utilizado con el nombre del array que contiene el psnr de este.
psnrDic={
'NN': '\psnrNN.npy',
'Lanczos3': '\psnrLan3.npy',
'Lanczos4': '\psnrLan4.npy',
'DCSRN': '\psnrSalv8.npy'
}

#Permite relacionar el método utilizado con el nombre del array que contiene el ssim de este.
ssimDic={
'NN': '\ssimNN.npy',
'Lanczos3': '\ssimLan3.npy',
'Lanczos4': '\ssimLan4.npy',
'DCSRN': '\ssimSalv8.npy'
}

# Crea un dataframe de los datos de una métrica utilizando el diccionario de PSNR o SSIM.
def crearConjuntoBigotes(dic):

    x = pd.DataFrame()
    for clave in dic:
        data = np.load(r"C:\Users\Estudiante\Documents\datasetMRI\final\pruebas\resultados"+dic[clave])
        df = pd.DataFrame(
            {'Metrica': data})
        df['Metodo'] = clave
        x = pd.concat([x, df])
    return x

# Crea un diagrama de cajas utilizando el diccionario de PSNR o SSIM.
def graficarBigotes(dic):
    x=crearConjuntoBigotes(dic)
    print(x)
    seaborn.set(style='whitegrid')
    seaborn.boxplot(x='Metodo', y='Metrica', data=x)
    plt.show()

# Estas listas contienen los resultados obtenidos por el modelo cada 50 epocas.
promPSNR=[29.91,33.97,37.51,37.86,37.89,37.91,37.89,37.93,37.89,37.91]
promSSIM=[0.81,0.82,0.85,0.87,0.89,0.90,0.90,0.90,0.90,0.90]

# Con base a una lista de entrada se crea un dataframe para graficar dicha información
def crearConjuntoHist(prom):
    df=pd.DataFrame()
    x=range(50,55*len(prom),50)
    df["Epoca"]=x
    df["SSIM promedio"]=prom
    return df

#Con base en una lista se grafica un diagrama de barras con dichos resultados.
def graficarHist(prom):
    data=crearConjuntoHist(prom)
    print(data)
    seaborn.barplot(x=data["Epoca"],y=data["PSNR promedio"], palette="Blues_d")
    plt.show()

#Con base en una lista se grafica una curva con dichos resultados.
def graficarCurva(prom):
    data=crearConjuntoHist(prom)
    print(data)
    seaborn.relplot(x=data["Epoca"],y=data["SSIM promedio"],kind="line", palette="Blues_d")
    plt.annotate("peso escogido", (data["Epoca"][3] + 0.7, data["SSIM promedio"][3]))
    plt.show(marker="s", ms=12, markevery=[0,1])


# Se selecciona la grafica que se desea obtener.
#graficarBigotes(ssimDic)
graficarCurva(promPSNR)
