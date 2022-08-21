import { ModeloUsuario } from "./modelo-usuario";

/**
 * Representa los datos de la imagen que será procesada
 */
export class ModeloImagen {
    //Identificador de la imagen
    public imagenId: number = 0;
    //Nombre de la imagen 
    public nombre: string = "";
    //Descripción breve hecha por el investigador
    public observacion: string = "";
    /**
     * Estado en el que se encuentra la imagen.
     * Puede tomar los siguientes valores:
     *  -SUBIDO
     *  -PROCESANDO
     *  -PROCESADO
     *  -DESCARGADO
     *  -ELIMINADO
     *  -ERROR
     *  -NO_ENCONTRADO
     *  -CANCELADO
     */
    public estado: string = "";
    //Descripción de los metadatos de la imagen en formato JSON
    public descripcionOriginal: string = "";
    //Ruta de AWS S3 donde se almacenará la imagen
    public rutaOriginal: string = "";
    //Fecha en que se cargó al sistema
    public fechaInicial: Date = new Date();
    //Fecha en que se eliminó del sistema
    public fechaEliminacion: Date = new Date();
    //Descripción de los metadatos de la imagen después del proceso en formato JSON
    public descripcionProcesada: string = "";
    //Ruta de AWS S3 donde se almacenará la imagen después del proceso
    public rutaProcesada: string = "";
    //Fecha en que se procesó
    public fechaProcesamiento: Date = new Date();
    //Investigador que cargó la imagen
    public usuario: ModeloUsuario = new ModeloUsuario(0, "", "", "",
        false, new Date(), true);

    constructor(imagenId: number, nombre: string, observacion: string, estado: string,
        descripcionOriginal: string, rutaOriginal: string, fechaInicial: Date,
        fechaEliminacion: Date, descripcionProcesada: string, rutaProcesada: string,
        fechaProcesamiento: Date, usuario: ModeloUsuario){
        this.imagenId = imagenId;
        this.nombre = nombre;
        this.observacion = observacion;
        this.estado = estado;
        this.descripcionOriginal = descripcionOriginal;
        this.rutaOriginal = rutaOriginal;
        this.fechaInicial = fechaInicial;
        this.fechaEliminacion = fechaEliminacion;
        this.descripcionProcesada = descripcionProcesada;
        this.rutaProcesada = rutaProcesada;
        this.fechaProcesamiento = fechaProcesamiento;
        this.usuario = usuario;
    }
}
