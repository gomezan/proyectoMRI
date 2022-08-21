import { HttpClient } from '@angular/common/http';
import { Component, Input, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { ModeloImagen } from 'src/app/model/modelo-imagen';
import { ModeloUsuario } from 'src/app/model/modelo-usuario';
import { LoginService } from 'src/app/shared/login.service';
import { ModeloImagenService } from 'src/app/shared/modelo-imagen.service';
import { ModeloUsuarioService } from 'src/app/shared/modelo-usuario.service';
import { ActivatedRoute, ParamMap, Router } from '@angular/router';
import { switchMap } from 'rxjs/operators';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { Response } from 'node-fetch';
import AWSS3UploadAshClient from 'aws-s3-upload-ash';
import { UploadResponse } from 'aws-s3-upload-ash/dist/types';
import { analyzeAndValidateNgModules } from '@angular/compiler';

@Component({
  selector: 'app-investigador',
  templateUrl: './investigador.component.html',
  styleUrls: ['./investigador.component.css']
})
export class InvestigadorComponent implements OnInit {
  //Usuario investigador que puede cargar o descargar imagenes
  usuario: ModeloUsuario | null = null;
  //Imagen seleccionada para ser descargada de AWS S3
  imagenDescarga: ModeloImagen | null = null;
  //Lista de imágenes pertenecientes al usuario
  imagenesDescargar: ModeloImagen[] = [];
  /**
   * Es el archivo imagen que se va a cargar a AWS S3.
   * Se diferencia de los atributos anteriores en que
   * ModeloImagen guarda la información de una imagen, mientras
   * que este atributo es la imagen como tal.
   */
  imagenCapturada: any | null = null;
  //Si es verdadero, muestra un elemento gráfico que indica que una imagen está cargandose
  uploadSpinner: boolean = false;
   //Si es verdadero, muestra un elemento gráfico que indica que una imagen está descargandose
  downloadSpinner: boolean = false;

  constructor(
    private http: HttpClient,
    private imagenService: ModeloImagenService,
    private loginService: LoginService,
    private usuarioService: ModeloUsuarioService,
    private route: ActivatedRoute,
    private _router: Router
  ) { }

  ngOnInit(): void {
    /**
     * Busca al investigador en la Base de Datos
     * Utiliza el parametro "iid" que representa el id del investigador
     */
    this.route.paramMap.pipe(switchMap(params => {
      let id = +params.get('iid')!;
      return this.usuarioService.findUsuarioById(id);
    })).subscribe(usuario => this.usuario = usuario);

    /**
     * Busca las imágenes del usuario, es decir,
     * las imágenes que éste ha cargado al sistema
     */
    this.route.paramMap.pipe(switchMap(params => {
      let id = +params.get('iid')!;
      return this.imagenService.findImagenesByUsuarioId(id);
    })).subscribe(imagenes => {
      this.imagenesDescargar = imagenes;
      this.ordenarImagenes();
    });
  }

  /**
   * Ordenar las imágenes por orden alfabético
   */

  ordenarImagenes(): void{
    let img: ModeloImagen|null = null;
    for(let i=0; i < this.imagenesDescargar.length-1; i++){
      for(let j=i+1; j < this.imagenesDescargar.length; j++){
        if(this.imagenesDescargar[i].imagenId > this.imagenesDescargar[j].imagenId){
          img = this.imagenesDescargar[i];
          this.imagenesDescargar[i] = this.imagenesDescargar[j];
          this.imagenesDescargar[j] = img;
        }
      }
    }
  }

  /**
   * Formulario para cargar una imagen.
   * Contiene: Observación de la imagen y el archivo que se quiere cargar. El archivo solamente puede ser NIFTI (.nii)
   */
  formularioCargarImagen = new FormGroup({
    observacion: new FormControl('', Validators.required),
    archivo: new FormControl('', Validators.required)
  });

  /**
   * Captura el archivo imagen
   */
  capturarImagen(event: any): any{
    //Evento donde se encuentra el archivo
    this.imagenCapturada = event.target.files[0]; 
    let split = this.imagenCapturada.name.split(".", 2);
    //Verifica que el archivo sea NIFTI
    if( split[1] !== "nii"){
      this.imagenCapturada = null;
      //Muestra un error
      this.mostrarError("inputImagen","errorImagen","Solo se aceptan archivos NIFTI (extensión .nii)");
      //Oculta un error
      setTimeout( () => this.ocultarError("inputImagen","errorImagen"), 10000);
    }
  }

  /**
   * Carga la imagen al sistema
   * @param observacion breve descripción hecha por el investigador
   */
  async cargarImagen(observacion: string){
    try{
      //Valida la observación y la imagen capturada
      let compObservacion = this.patronRegex(observacion, environment.REGEX_OBSERVACION);

      if(this.imagenCapturada && compObservacion){
        //Hace una confirmación
        if(confirm("La imagen " + this.imagenCapturada.name + " será cargada al sistema para ser procesada ¿desea continuar?")){
          //Llama al servicio AWS S3
          await this.uploadToAWSS3(this.imagenCapturada).then(()=>{
            //Genera la descripción de la imagen basandose en su información
          const descripcion = this.stringify(this.imagenCapturada);
          //Es la ruta de AWS S3 donde será almacenada
          let ruta = "s3://" + environment.BUCKET_NAME + "/" + environment.IMAGENES_NO_PROCESADAS + "/" + this.imagenCapturada.name;
          let rutaProcesada = "s3://" + environment.BUCKET_NAME + "/" + environment.IMAGENES_PROCESADAS + "/" + this.imagenCapturada.name;
          //Llama al servicio de imagen
          this.imagenService.postImagen(
            new ModeloImagen(0, this.imagenCapturada.name, observacion, "SUBIDO", 
            descripcion, ruta, new Date(), new Date(), descripcion, 
            rutaProcesada, new Date(), this.usuario!)
          ).subscribe(()=>{
            this.imagenService.findImagenesByUsuarioId(this.usuario!.usuarioId).subscribe(imagenes =>{
              this.imagenesDescargar = imagenes;
              this.ordenarImagenes();
            })
          });
          //El formulario vuelve a sus estado inicial como si nada hubiese pasado
          this.formularioCargarImagen.reset();
          this.imagenCapturada = null;
          })
          .catch((err: any) =>{
              throw err;
          });
        }
      }
      else{
        //Muestra los errores cometidos por el usuario y los oculta
        if(this.imagenCapturada == null){
          this.mostrarError("inputImagen","errorImagen","No ha seleccionado ninguna imagen para subir");
          setTimeout( () => this.ocultarError("inputImagen","errorImagen"), 10000);
        }
        if(!compObservacion){
          this.mostrarError("inputObservacion","errorObservacion", "Ingrese un comentario<br>Máximo 6 palabras");
          setTimeout( () => this.ocultarError("inputObservacion","errorObservacion"), 10000);
        }
      }
    }
    catch(err){
      //En caso de que la imagen no se pueda cargar muestra un error
      this.mostrarError("btnCargar","errorCargar","La imagen no pudo ser cargada");
      //Oculta el error
      setTimeout( () => this.ocultarError("btnCargar","errorCargar"), 10000);
      //Limpia la consola
      console.clear();
    }
  }

  /**
   * Función para generar la descripción de la imagen
   * @param obj es la imagen capturada
   * @returns la descripción de la imagen
   */
  stringify(obj: File): string {
    const replacer = [];
    for (const key in obj) {
        replacer.push(key);
    }
    return JSON.stringify(obj, replacer);
  }  

  /**
   * Selecciona una imagen de la lista de imágenes
   * @param imagen 
   */
  seleccionarImagenDescarga(imagen: ModeloImagen): void{
    this.imagenDescarga = imagen;
  }

  /**
   * Descargar la imagen de AWS S3
   */
  async descargarImagen(){
    try{
      if(this.imagenDescarga){
        //La imagen solo puede descargarse si está en estado PROCESADO o DESCARGADO
       if(this.imagenDescarga!.estado === "PROCESADO" || this.imagenDescarga!.estado === "DESCARGADO"){
          //Llama al servicio AWS S3
          await this.downloadFromAWSS3(this.imagenDescarga!.nombre).then(()=>{
            //Actualiza el estado de la imagen
            this.imagenService.putDescargarImagen(this.imagenDescarga!.imagenId).subscribe(()=>{
              this.imagenService.findImagenesByUsuarioId(this.usuario!.usuarioId).subscribe(imagenes =>{
                this.imagenesDescargar = imagenes;
                this.ordenarImagenes();
              })
            });
            this.imagenDescarga = null;
          })
          .catch((err: any) => {
            throw err;
          });
        }
        else if(this.imagenDescarga!.estado === "SUBIDO" || this.imagenDescarga!.estado === "PROCESANDO"){
          //Muestra un error en caso de que la imagen aún no haya sido procesada
          this.mostrarError("tableIrms","errorIrms", "La imagen aún no ha sido procesada");
          //Oculta el error
          setTimeout( () => this.ocultarError("tableIrms","errorIrms"), 10000);
        }
        else{
          //Muestra un error en caso de que la imagen haya sido eliminada del sistema
          this.mostrarError("tableIrms","errorIrms", "La imagen ya no se encuentra disponible");
          //Oculta el error
          setTimeout( () => this.ocultarError("tableIrms","errorIrms"), 10000);
        }
      }
      else{
        //Muestra un error en caso de que no se haya seleccionado una imagen
        if(this.imagenDescarga == null){
          this.mostrarError("tableIrms","errorIrms", "Seleccione una imagen de la tabla");
          //Oculta el error
          setTimeout( () => this.ocultarError("tableIrms","errorIrms"), 10000);
        }
      }
    }
    catch(err){
      //Muestra un error en caso de que la imagen no se haya podido descargar
      this.mostrarError("btnDescargar","errorDescargar","La imagen no pudo ser descargada");
      //Oculta el error
      setTimeout( () => this.ocultarError("btnDescargar","errorDescargar"), 10000);
      //Limpia la consola
      console.clear();
    }
  }

  /**
   * Compara un parámetro con un patrón para verificar si el parámetro es válido
   * @param param Representa el parametro capturado en un elemento Input
   * @param regex Representa el patrón con el que se va a comparar el parámetro
   * @returns 
   */
   patronRegex(param: string, regex:any): boolean{
    let comp = param.match(regex);
    if(comp?.length == 1)
      return true;
    else 
      return false;
  }
  
  /**
   * Despliega un mensaje de error en la pantalla, de modo que el usuario pueda saber en donde se equivocó
   * @param idElement Elemento al que corresponde el error
   * @param idError id del elemento Span que va a mostrar el error
   * @param mensaje Mensaje de error que se desplegará por pantalla
   */
  mostrarError(idElement: string, idError: string, mensaje: string): void {
    var error = document.getElementById(idError);
    error!.setAttribute("style","display:inline;");
    error!.setAttribute("aria-invalid","true");
    error!.innerHTML="&nbsp;<b>ERROR</b> - " + mensaje;
    document.getElementById(idElement!)!.setAttribute("aria-invalid", "true");
  }

  /**
   * Oculta un mensaje de error
   * @param idElement Elemento al que corresponde el error
   * @param idError id del elemento Span que va a ocultar el error
   */
  ocultarError(idElement: string, idError: string): void {
    var error = document.getElementById(idError);
    error!.setAttribute("style","display:none;");
    error!.setAttribute("aria-invalid","false");
    error!.innerHTML="";
    document.getElementById(idElement!)!.setAttribute("aria-invalid", "false");
  }

  /**
   * Despliega un mensaje de error en la pantalla, de modo que el usuario pueda saber en donde se equivocó
   * @param idElement Elemento al que corresponde el error
   * @param idError id del elemento Span que va a mostrar el error
   * @param mensaje Mensaje de error que se desplegará por pantalla
   */
   mostrarSuccess(idElement: string, idSuccess: string, mensaje: string): void {
    var success = document.getElementById(idSuccess);
    success!.setAttribute("style","display:inline;");
    success!.setAttribute("aria-invalid","true");
    success!.innerHTML="&nbsp;<b>ÉXITO</b> - " + mensaje;
    document.getElementById(idElement!)!.setAttribute("aria-invalid", "true");
  }

  /**
   * Oculta un mensaje de error
   * @param idElement Elemento al que corresponde el error
   * @param idError id del elemento Span que va a ocultar el error
   */
  ocultarSuccess(idElement: string, idSuccess: string): void {
    var success = document.getElementById(idSuccess);
    success!.setAttribute("style","display:none;");
    success!.setAttribute("aria-invalid","false");
    success!.innerHTML="";
    document.getElementById(idElement!)!.setAttribute("aria-invalid", "false");
  }

  /**
   * Cierra la sesión
   */
  logout(): void{
    //Llama al servicio de Logout
    this.loginService.logout();
    let url = "login";
    this._router.navigate([url]);
  }

   /**
   * Configuración de AWS S3, es necesario para poder acceder al servidor.
   */
    config = {
      bucketName: environment.BUCKET_NAME,
      dirName: environment.IMAGENES_NO_PROCESADAS,
      region: environment.REGION_NAME,
      accessKeyId: environment.AWS_ACCESS_KEY_ID,
      secretAccessKey: environment.AWS_ACCESS_KEY_SECRET,
      s3Url: environment.URL_AWS_S3,
      accessControlAllowOrigin: environment.ACCESS_CONTROL_ALLOW_ORIGIN
    };
    //Cliente S3
    S3CustomClient: AWSS3UploadAshClient = new AWSS3UploadAshClient(this.config);
  
  
    /**
     * Carga una imagen a AWS S3
     * @param imagen 
     */
    async uploadToAWSS3(imagen: any){
      //Inicializa el Spinner
      this.uploadSpinner = true;
      //Carga la imagen
      await this.S3CustomClient
      .uploadFile(imagen, imagen.type, undefined, imagen.name, "public-read")
      .then((data: UploadResponse) => {
        //Termina el spinner
        this.uploadSpinner = false;
        //Muestra un mensaje de éxito
        this.mostrarSuccess("inputImagen","successCargar", "La imagen se ha subido");
        //Oculta un mensaje de éxito
        setTimeout( () => this.ocultarSuccess("inputImagen","successCargar"), 10000);
      })
      .catch((err: any) => {
        //Termina el spinner
        this.uploadSpinner = false;
        //Limpia la consola
        console.clear();
        throw err;
      }); 
    }
  
    /**
     * Descarga una imagen de AWS S3
     * @param nombreImagen 
     */
    async downloadFromAWSS3(nombreImagen: string){
      //Inicializa el Spinner
      this.downloadSpinner = true;
      try{
        //Utiliza la librería 'aws-sdk/clients/s3'
        const S3 = require('aws-sdk/clients/s3');
        //Es para la imagen en el disco
        const FileSaver = require('file-saver');
        //Crea S3 con la siguiente configuración
        const s3 =  new S3({
          apiVersion: environment.AWS_S3_API_VERSION,
          region: environment.REGION_NAME,
          accessKeyId: environment.AWS_ACCESS_KEY_ID,
          secretAccessKey: environment.AWS_ACCESS_KEY_SECRET
        });
        
        /**
         * Key representa la dirección donde se encuentra la imagen.
         * nombre_carpeta/nombre_imagen
         * En caso de que no se encuentre dentro de un directorio, solo se 
         * coloca el nombre de la imagen
         */
        const param = {
          Bucket: environment.BUCKET_NAME,
          Key: environment.IMAGENES_PROCESADAS + "/" + nombreImagen
        }
        
        //Guarda la respuesta de la petición para pedir la imagen
        let obj = await s3.getObject(param).promise();
        /**
         * Separa el nombre de la imagen de su extensión
         * [0: nombre_imagen] [1: Extension{png, jpg, jpeg, nii, dcm}]
         */
        let splits = nombreImagen.split(".", 2);
        const imgType = "image/" + splits[1]; 
  
        //Obtiene la imagen de la respuesta y le asigna un tipo de imagen
        const blob = new Blob([obj['Body']], { type: imgType });
        //Almacena la imagen en el disco
        FileSaver.saveAs(blob, nombreImagen);
        //Termina el Spinner
        this.downloadSpinner = false;
        //Muestra un mensaje de éxito
        this.mostrarSuccess("tableIrms","successIrms", "La imagen ha sido descargada");
        //Oculta un mensaje de éxito
        setTimeout( () => this.ocultarSuccess("tableIrms","successIrms"), 10000);
        
      }
      catch(err){
        //Termina el Spinner
        this.downloadSpinner = false;
         //Limpia la consola
         console.clear();
        throw err;
      }
    }

}
