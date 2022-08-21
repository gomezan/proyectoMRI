
# Es el paquete que contiene toda la información de la imagen de la misma forma que lo maneja el back-end

class ImagenDto():
    fechaEliminacion: None
    estado: None
    rutaOriginal: None
    fechaInicial: None
    fechaProcesamiento: None
    rutaProcesada: None
    descripcionProcesada: None
    imagenId: None
    nombre: None
    observacion: None
    descripcionOriginal: None
    

    def __init__(self, my_dict):
        self.imagenId = my_dict['imagenId']
        self.nombre = my_dict['nombre']
        self.observacion = my_dict['observacion']
        self.estado = my_dict['estado']
        self.descripcionOriginal = my_dict['descripcionOriginal']
        self.rutaOriginal = my_dict['rutaOriginal']
        self.fechaInicial = my_dict['fechaInicial']
        self.fechaEliminacion = my_dict['fechaEliminacion']
        self.descripcionProcesada = my_dict['descripcionProcesada']
        self.rutaProcesada = my_dict['rutaProcesada']
        self.fechaProcesamiento = my_dict['fechaProcesamiento']

    def setDescipcionProcesada(self,DescipcionProcesada):
        self.descripcionProcesada=DescipcionProcesada

    def setRutaProcesada(self, RutaProcesada):
        self.rutaProcesada=RutaProcesada

    def setFechaProcesamiento(self,FechaProcesamiento):
        self.fechaProcesamiento=FechaProcesamiento

    def setEstado(self, Estado):
        self.estado=Estado

    def getRutaOriginal(self):
        return self.rutaOriginal

