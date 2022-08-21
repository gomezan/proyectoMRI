/**
 * Representa al usuario del sistema. Puede ser un investigador o administador.
 */
export class ModeloUsuario {
    //Identificador del usuario
    public usuarioId: number = 0;
    //Nombre del usuario
    public nombre: string = "";
    //Correo
    public correo: string = "";
    //Contraseña
    public clave: string = "";
    //Indica si es el administrador o no
    public administrador: boolean = false;
    //Fecha en que el usuario fue creado
    public fechaCreacion: Date = new Date();
    /**
     * Indica si el usuario está habilitado o no.
     * Si está habilitado, puede ingresar al sistema 
     * */ 
    public habilitado: boolean = false;

    constructor(usuarioId: number, nombre: string, correo: string, clave: string,
        administrador: boolean, fechaCreacion: Date, habilitado: boolean){
            this.usuarioId = usuarioId;
            this.nombre = nombre;
            this.correo = correo;
            this.clave = clave;
            this.administrador = administrador;
            this.fechaCreacion = fechaCreacion;
            this.habilitado = habilitado;
    }
}
