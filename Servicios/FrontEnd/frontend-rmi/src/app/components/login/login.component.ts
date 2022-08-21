import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { ModeloUsuario } from 'src/app/model/modelo-usuario';
import { LoginService } from 'src/app/shared/login.service';
import { ModeloUsuarioService } from 'src/app/shared/modelo-usuario.service';
import { ActivatedRoute, ParamMap, Router } from '@angular/router';
import { switchMap } from 'rxjs/operators';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { map } from 'rxjs/operators';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  /**
   * Usuario que busca iniciar sesión
   */
  usuario: ModeloUsuario | null = null;

  constructor(
    private usuarioService: ModeloUsuarioService,
    private loginService: LoginService,
    private route: ActivatedRoute,
    private _router: Router
  ) { }

  ngOnInit(): void {
  }

  /**
   * Formulario Iniciar Sesión
   * Contiene: Correo y contraseña
   */
  formularioIniciarSesion = new FormGroup({
    correo: new FormControl('', Validators.required),
    contrasena: new FormControl('', Validators.required)
  });

  /**
   * Permite que el usuario inicie sesión en el sistema
   * @param correo 
   * @param contrasena 
   */
  login(correo: string, contrasena: string): void{
    //Hace la validación del correo y la contraseña
    let condCorreo = this.patronRegex(correo, environment.REGEX_CORREO);
    let condContrasena = this.patronRegex(contrasena, environment.REGEX_CONTRASENA);

    if(condCorreo && condContrasena){
      //Llama servicio de login
      this.loginService.login(
        new ModeloUsuario(0, "", correo, contrasena,
        false, new Date(), false)
      )
      .subscribe((usuario) => {
        this.usuario! = usuario;
        //Autentica al usuario
        this.loginService.setIsAuth(true);
        //Salva los datos del usuario
        if(this.usuario!.administrador)
          this.loginService.saveAuthData(this.usuario!.usuarioId, "administrador");
        else
        this.loginService.saveAuthData(this.usuario!.usuarioId, "investigador");
        //Redirige al Home del usuario
        this.redirigir();
      }, (error: any) => {
        if(error.status === 403){
          //Muestra un error en caso de que el usuario esté deshabilitado
          this.mostrarError("btnIniciarSesion", "errorIniciarSesion", "Usuario deshabilitado, consulte con el administrador");
        }
        else if(error.status === 404){
          //Muestra un error en caso de no encontrar al usuario
          this.mostrarError("btnIniciarSesion", "errorIniciarSesion", "El usuario no aparece registrado");
        }
        else{
          //Muestra un error en caso de no encontrar al usuario
          this.mostrarError("btnIniciarSesion", "errorIniciarSesion", "No es posible iniciar sesión en este momento");
        }
        //Oculta el error
        setTimeout( () => this.ocultarError("btnIniciarSesion", "errorIniciarSesion"), 10000);
        //Limpia la consola
        console.clear();
      });
    }
    else{
      //Muestra los errores cometidos por el usuario
      if(!condCorreo){
        this.mostrarError("inputCorreo", "errorCorreo", "El correo no es válido");
        //Oculta el error
        setTimeout( () => this.ocultarError("inputCorreo", "errorCorreo"), 10000);
      }
      if(!condContrasena){
        this.mostrarError("inputContrasena", "errorContrasena", "La contraseña no es válida");
         //Oculta el error
         setTimeout( () => this.ocultarError("inputContrasena", "errorContrasena"), 10000);
      }
    }
    //Limpia la consola
    console.clear();
  }
  /**
   * Redirige al Home del usuario
   */
  redirigir(): void{
    let url = "";
    if(this.usuario!.administrador){
      //En caso de ser administrador
      url = "home/" + this.usuario!.usuarioId +"/administrador";
    }
    else{
      //En caso de ser investigador
      url = "home/" + this.usuario!.usuarioId +"/investigador";
    }
    this._router.navigate([url]);
  }

  /**
   * Compara un parámetro con un patrón para verificar si el parámetro es válido
   * @param param Representa el parámetro capturado en un elemento Input
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
}
