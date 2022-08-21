import { Component, Input, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { ModeloUsuario } from 'src/app/model/modelo-usuario';
import { LoginService } from 'src/app/shared/login.service';
import { ModeloUsuarioService } from 'src/app/shared/modelo-usuario.service';
import { ActivatedRoute, ParamMap, Router } from '@angular/router';
import { switchMap } from 'rxjs/operators';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-gestionar-investigador',
  templateUrl: './gestionar-investigador.component.html',
  styleUrls: ['./gestionar-investigador.component.css']
})
export class GestionarInvestigadorComponent implements OnInit {
  //El usuario administrador que puede gestionar investigadores dentro del sistema.
  administrador: ModeloUsuario | null = null;
  //El usuario investigador cuyos datos serán gestionados
  investigador: ModeloUsuario | null = null;

  constructor(
    private usuarioService: ModeloUsuarioService,
    private loginService: LoginService,
    private route: ActivatedRoute,
    private _router: Router
  ) { }

  ngOnInit(): void {
    /**
     * Busca al investigador en el sistema
     * Utiliza el parametro "iid" que representa el id del investigador
     */
    this.route.paramMap.pipe(switchMap(params => {
      let id = +params.get('iid')!;
      return this.usuarioService.findUsuarioById(id);
    })).subscribe(usuario => {
      this.investigador = usuario;
      /**
       * Coloca los datos del investigador dentro de los inputs del html,
       * esto con el objetivo de ayudar al administrador para que pueda hacer las
       * modificaciones pertienentes y de manera correcta.
       * 
       * La clave no se muestra
       */
      this.formularioGestionarInvestigador.get('nombre')!.setValue(this.investigador!.nombre);
      this.formularioGestionarInvestigador.get('correo')!.setValue(this.investigador!.correo);
      this.formularioGestionarInvestigador.get('contrasena')!.setValue("");
      this.formularioGestionarInvestigador.get('confirmacion')!.setValue("");
    });

    /**
     * Busca al administrador en el sistema
     * Utiliza el parametro "aid" que representa el id del administrador
     */
    this.route.paramMap.pipe(switchMap(params => {
      let id = +params.get('aid')!;
      return this.usuarioService.findUsuarioById(id);
    })).subscribe(usuario => this.administrador = usuario);
  }

 /**
   * Formulario de Gestionar Investigador
   * Contiene: Nombre, correo, contraseña y confirmación de contraseña
   */
  formularioGestionarInvestigador = new FormGroup({
    nombre: new FormControl('', Validators.required),
    correo: new FormControl('', Validators.required),
    contrasena: new FormControl('', Validators.required),
    confirmacion: new FormControl('', Validators.required)
  });
  /**
   * Edita los datos de un investigador y lo guarda
   * @param nombre 
   * @param correo 
   * @param contrasena 
   * @param confirmacion 
   */
  guardarInvestigador(nombre: string, correo: string, contrasena: string, confirmacion: string): void{
    //Banderas de control para saber qué datos se han cambiado y han sido aprobados
    let cambioDatosBasicos = false;
    let aprobadoDatosBasicos = false;
    let cambioClave = false;
    let aprobadaClave = false;

    //El nombre y el correo deben ser distintos a los datos ya registrados, de lo contrario
    //significa que el administrador no ha hecho cambios
    if(this.investigador!.nombre !== nombre || this.investigador!.correo !== correo){
      cambioDatosBasicos = true;
      //Valida el nombre y el correo
      let compNombre = this.patronRegex(nombre, environment.REGEX_NOMBRE);
      let compCorreo = this.patronRegex(correo, environment.REGEX_CORREO);
      
      if(compNombre && compCorreo){
        //Solo puede continuar si la contraseña y su confirmación son iguales
          this.investigador!.nombre = nombre;
          this.investigador!.correo = correo;
          this.investigador!.clave = contrasena;
          aprobadoDatosBasicos = true;
        }
      else{
        //Muestra los errores cometidos por el usuario
        if(!compNombre){
          this.mostrarError("inputNombre", "errorNombre", "Ejemplo: Manuela Beltrán Camacho <br> Primera letra en mayúscula");
          //Oculta un error
          setTimeout( () => this.ocultarError("inputNombre", "errorNombre"), 10000);
        }
        if(!compCorreo){
          this.mostrarError("inputCorreo", "errorCorreo", "Formato: nombre@servidorcorreo.dominio<br> Puede usar: punto, guion o guion bajo");  
           //Oculta un error
           setTimeout( () => this.ocultarError("inputCorreo", "errorCorreo"), 10000);
        }
        aprobadoDatosBasicos = false;
      }
    }
    //La contraseña y su confirmación deben ser distintas a string vacio
    if(contrasena !== "" || confirmacion !== ""){
      cambioClave = true;
      //Válida la contraseña
      let compContrasena = this.patronRegex(contrasena, environment.REGEX_CONTRASENA);
      let compConfirmacion = this.patronRegex(confirmacion, environment.REGEX_CONTRASENA);
      if(compContrasena && compConfirmacion){
        //La clave y la confirmación deben ser iguales
          if(contrasena === confirmacion){
            aprobadaClave = true;
          }
          else{
            //Error que indica que la contraseña y su confirmación son distintas
            this.mostrarError("inputConfirmacionContrasena", "errorConfirmacionContrasena", "La contraseña y su confirmación son distintas");  
            //Oculta un error
            setTimeout( () => this.ocultarError("inputConfirmacionContrasena", "errorConfirmacionContrasena"), 10000);
            aprobadaClave = false;
          }
      }
      else{
        //Muestra los errores relacionados con la contraseña
        if(!compContrasena){
          this.mostrarError("inputContrasena", "errorContrasena", "Puede usar: letras, números,<br>punto, guion o guion bajo");
          //Oculta un error
          setTimeout( () => this.ocultarError("inputContrasena", "errorContrasena"), 10000);
        }
        if(!compConfirmacion){
          this.mostrarError("inputConfirmacionContrasena", "errorConfirmacionContrasena", "La confirmación no es válida");
          //Oculta un error
          setTimeout( () => this.ocultarError("inputConfirmacionContrasena", "errorConfirmacionContrasena"), 10000);
        }
        aprobadaClave = false;
      }
     
    }

    //En caso de que todos los datos hayan sido cambiados y aprobados
    if(cambioDatosBasicos && aprobadoDatosBasicos && cambioClave && aprobadaClave){
      //Llama al servicio para guardar los datos del investigador
      this.usuarioService.putAdmin(
        this.investigador!
      ).subscribe(()=>{
        //Regresa al Home
        this.volver();
      });
      //Llama al servicio para guardar la clave del investigador
      //Por cuestiones de seguridad, la contraseña o clave se actualiza de manera distinta
      this.usuarioService.putClaveUsuario(
        new ModeloUsuario(this.investigador!.usuarioId, "",
        "", contrasena, false, new Date(), true)
      ).subscribe(()=>{
        //Regresa al Home
        this.volver();
      });
    }
    //En caso de que solo se haya cambiado el nombre y el correo
    else if(cambioDatosBasicos && aprobadoDatosBasicos && !cambioClave){
      //Llama al servicio para guardar los datos del investigador
      this.usuarioService.putAdmin(
        this.investigador!
      ).subscribe(()=>{
        //Regresa al Home
        this.volver();
      });
    }
    //En caso de que solo se haya cambiado la contraseña
    else if(cambioClave && aprobadaClave && !cambioDatosBasicos){
       //Llama al servicio para guardar la clave del investigador
      //Por cuestiones de seguridad, la contraseña o clave se actualiza de manera distinta
     this.usuarioService.putClaveUsuario(
        new ModeloUsuario(this.investigador!.usuarioId, "",
        "", contrasena, false, new Date(), true)
      ).subscribe(()=>{
        //Regresa al Home
        this.volver();
      });
    }
    
  }

  /**
   * Habilita al investigador para que pueda ingresar al sistema
   */
  habilitarInvestigador(): void{
    this.investigador!.habilitado = true;
    /**
     * Utiliza el servicio de usuario
     */
    this.usuarioService.putAdmin(
      this.investigador!
    ).subscribe();
    this.volver();
  }

  /**
   * Deshabilita al investigador para que no pueda ingresar al sistema
   */
  deshabilitarInvestigador(): void{
    this.investigador!.habilitado = false;
    /**
     * Utiliza el servicio de usuario
     */
    this.usuarioService.putAdmin(
      this.investigador!
    ).subscribe();
    this.volver();
  }

  /**
   * Vuelve al Home del administrador
   */
  volver(): void{
    let url = "home/" + this.administrador!.usuarioId +"/administrador";
    this._router.navigate([url]);
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
   * Cierra la sesión
   */
   logout(): void{
     //Llama al servicio de logout
    this.loginService.logout();
    let url = "login";
    this._router.navigate([url]);
  }
}
