Este Readme es una descripción de las funciones de cada uno de los scripts dentro de la carpeta
y un breve manual para la creación y/o modificación del conjunto de datos.

*comprimidor: Este se encarga de compactar todos los parches en un solo archivo npy. Puede usarse para crear el ground truth o las imagenes decimadas de acuerdo a su entrada.

*cortador: Toma todos los archivos .npy de una locación dada de entrada y recorta los bordes en tres dimensiones de estos.
Luego almacena el resultado en un directorio de salida.

*creadorLR: Toma todos los archivos .npy de una locación dada de entrada y realiza el proceso de decimación sobre estos.
En escencia se encarga de filtrar y submuestrear dichas imagenes. Luego almacena el resultado en un directorio de salida.

*creadorModeloDatasets: Dados los pesos de la red contenidos en una carpeta. Este Toma todos los archivos .npy de una locación dada de entrada y realiza el proceso de super-resolución sobre estos.
Luego almacena el resultado en un directorio de salida.

*data-augmented: Este es el script original de Omagdy para obtener parches de una imagen .npy. 
Este Toma todos los archivos .npy de una locación dada de entrada y obtiene x parches de cada uno. Luego almacena los parches obtenidos en un directorio de salida.

*expandidor: Toma todos los archivos .npy de una locación dada de entrada y realiza el proceso de interpolación sobre estos.
En este se encuentran los métodos de vecinos más cercanos y lanczos de forma que se puede utilizar cualquiera de los dos. Luego almacena el resultado en un directorio de salida.

*nii2npy:  Toma todos los archivos .nii de una locación dada de entrada y realiza el proceso de conversión a npy sobre estos.
Luego almacena el resultado en un directorio de salida.

*parchado: Este script se encarga de obtener los parches de las imagenes en formato npy. 
Este es una variante del script data-augmented.py pero en vez de obtener parches de una única imagen, este obtiene parches en paralelo de las imagenes decimadas y las imagenes del ground truth.
Es necesario suministrar como entrada las ubicaciones de ambos directorios. 
La razón de que este proceso se realice en paralelo radica en que los parches deben obtenerse de forma aleatoria pero las imágenes representadas en los parches deben ser las mismas entre ambos conjuntos. 

*test: Este script implementa el PSNR y el SSIM para realizar pruebas sobre los métodos de interpolación y el modelo.
Es necesario tener las ubicaciones de las carpetas donde se encuentran las imagenes en formato .nii.   

*graficador: Este script permite graficar resultados obtenidos del scrip test.py.

**********************************
MANUAL CREACIÓN CONJUNTO DE DATOS
**********************************

1. Utilizar el script nii2npy.py para convertir las imágenes a .npy. Estas son el ground truth.
2. Utilizar el script creadorLR.py sobre las imágenes en el númeral anterior para obtener las imagenes decimadas.
3. Utilizar el script expandidor.py sobre las imágenes en el númeral anterior para obtener las imagenes interpoladas.
4. Utilizar el script parchado.py sobre las imágenes en el númeral anterior y el numeral 1 para obtener los parches de las imágenes.
5. Utilizar el script cortador.py para recortar los bordes de ambos grupos de paches, tanto los del ground truth como los de las imágenes decimadas. 
6. Utilizar el script comprimidor.py para unir todos los parches en un mismo archivo, tanto los del ground truth como los de las imágenes decimadas. 