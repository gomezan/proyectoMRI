
import sys

if __name__ == '__main__':

    conversor=r"C:\Users\Estudiante\PycharmProjects\pruebaModelos\DCSRNyunzeman\NII2NPY\nii2npy.py"
    aumentador=r"C:\Users\Estudiante\PycharmProjects\pruebaModelos\DCSRNyunzeman\NII2NPY\data_augment.py"
    comprimidor=r"C:\Users\Estudiante\PycharmProjects\pruebaModelos\DCSRNyunzeman\comprimidor.py"
    decimador=r"C:\Users\Estudiante\PycharmProjects\pruebaModelos\DCSRNyunzeman\creadorLR.py"
    expandidor=r"C:\Users\Estudiante\PycharmProjects\pruebaModelos\DCSRNyunzeman\expandidor.py"
    cortador=r"C:\Users\Estudiante\PycharmProjects\pruebaModelos\DCSRNomagdy\cortador.py"

    red=r"C:\Users\Estudiante\PycharmProjects\pruebaModelos\DCSRNomagdy\DCSRNmain\dcsrn.py"
    test=r"C:\Users\Estudiante\Documents\GitHub\tesis\pruebaModelos\DCSRNomagdy\DCSRNmain\test.py"
    datsasetModelo=r"C:\Users\Estudiante\PycharmProjects\pruebaModelos\DCSRNomagdy\creadorModeloDatasets.py"

    seg=r"C:\Users\Estudiante\PycharmProjects\pruebaModelos\DCSRNyunzeman\NII2NPY\segmentacion.py"
    graph=r"C:\Users\Estudiante\Documents\GitHub\tesis\pruebaModelos\DCSRNomagdy\DCSRNmain\graficador.py"


    archivoExec = graph
    source_code = open(archivoExec).read()
    sys.argv = [archivoExec]
    exec(source_code)
