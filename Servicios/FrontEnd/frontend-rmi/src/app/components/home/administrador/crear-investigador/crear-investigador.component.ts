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
  selector: 'app-crear-investigador',
  templateUrl: './crear-investigador.component.html',
  styleUrls: ['./crear-investigador.component.css']
})
export class CrearInvestigadorComponent implements OnInit {
  /**
   * El usuario administrador que puede crear investigadores dentro
   * del sistema.
   */
  administrador: ModeloUsuario | null = null;

  constructor(
    private usuarioService: ModeloUsuarioService,
    private loginService: LoginService,
    private route: ActivatedRoute,
    private _router: Router
  ) { }

  ngOnInit(): void {
    /**
     * Busca al administrador
     * Utiliza el parametro "aid" que representa el id del administrador
     */
    this.route.paramMap.pipe(switchMap(params => {
      let id = +params.get('aid')!;
      return this.usuarioService.findUsuarioById(id);
    })).subscribe(usuario => this.administrador = usuario);
  }
  /**
   * Formulario de Crear Investigador
   * Contiene: Nombre, correo, contraseña y confirmación de contraseña
   */
  formularioCrearInvestigador = new FormGroup({
    nombre: new FormControl('', Validators.required),
    correo: new FormControl('', Validators.required),
    contrasena: new FormControl('', Validators.required),
    confirmacion: new FormControl('', Validators.required)
  });

  /**
   * Crea un nuevo investigador y lo guarda en el sistema
   * @param nombre 
   * @param correo 
   * @param contrasena 
   * @param confirmacion 
   */
  nuevoInvestigador(nombre: string, correo: string, contrasena: string, confirmacion: string): void{
    //Valida el nombre, el correo y la contraseña
    let compNombre = this.patronRegex(nombre, environment.REGEX_NOMBRE);
    let compCorreo = this.patronRegex(correo, environment.REGEX_CORREO);
    let compContrasena = this.patronRegex(contrasena, environment.REGEX_CONTRASENA);
    let compConfirmacion = this.patronRegex(confirmacion, environment.REGEX_CONTRASENA);
    if(compNombre && compCorreo && compContrasena && compConfirmacion){
      //Solo puede continuar si la contraseña y su confirmación son iguales
      if(contrasena === confirmacion){
        //Hace una confirmación
        if(confirm("El investigador " + nombre + " con correo " + correo + " será registrado en el sistema ¿está de acuerdo?")){
          /**
           * Utiliza el servicio de usuario
           */
          this.usuarioService.postCrearUsuario(
            new ModeloUsuario(0, nombre, correo, contrasena, false, new Date(), true)
          ).subscribe(()=>{
            //Regresa al Home
            this.volver();
          });
        }
      }
      else{
        this.mostrarError("inputConfirmacionContrasena", "errorConfirmacionContrasena", "La contraseña y su confirmación son distintas");
        //Oculta un error
       setTimeout( () => this.ocultarError("inputConfirmacionContrasena", "errorConfirmacionContrasena"), 10000);
      }
    }
    else{
      //Muestra los errores cometidos por el usuario según sea el caso
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
    }
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
