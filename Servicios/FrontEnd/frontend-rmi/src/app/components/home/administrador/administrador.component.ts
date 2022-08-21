import { Component, Input, OnInit } from '@angular/core';
import { ModeloUsuario } from 'src/app/model/modelo-usuario';
import { LoginService } from 'src/app/shared/login.service';
import { ModeloUsuarioService } from 'src/app/shared/modelo-usuario.service';
import { ActivatedRoute, ParamMap, Router } from '@angular/router';
import { switchMap } from 'rxjs/operators';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-administrador',
  templateUrl: './administrador.component.html',
  styleUrls: ['./administrador.component.css']
})
export class AdministradorComponent implements OnInit {
  //El usuario administrador que puede gestionar investigadores dentro del sistema.
  administrador: ModeloUsuario | null = null;
  //El usuario investigador seleccionado para ser editado
  investigadorSelect: ModeloUsuario | null = null;
  //Todos los investigadores registrados en el sistema
  investigadores: ModeloUsuario[] = [];

  constructor(
    private usuarioService: ModeloUsuarioService,
    private loginService: LoginService,
    private route: ActivatedRoute,
    private _router: Router
  ) { }

  ngOnInit(): void {
     /**
     * Busca al administrador en la Base de Datos
     * Utiliza el parametro "aid" que representa el id del administrador
     */
    this.route.paramMap.pipe(switchMap(params => {
      let id = +params.get('aid')!;
      return this.usuarioService.findUsuarioById(id);
    })).subscribe(usuario => this.administrador = usuario);
    /**
     * Busca a todos los investigadores registrados en el sistema
     */
    this.usuarioService.findAllInvestigadores()
    .subscribe(investigadores => {
      this.investigadores = investigadores;
      this.ordenarInvestigadores();
    });
  }

  /**
   * Ordenar los investigadores por orden alfabético
   */

   ordenarInvestigadores(): void{
    let us: ModeloUsuario|null = null;
    for(let i=0; i < this.investigadores.length-1; i++){
      for(let j=i+1; j < this.investigadores.length; j++){
        if(this.investigadores[i].nombre > this.investigadores[j].nombre){
          us = this.investigadores[i];
          this.investigadores[i] = this.investigadores[j];
          this.investigadores[j] = us;
        }
      }
    }
  }

  /**
   * Crea un nuevo investigador
   */
  nuevoInvestigador(): void{
    let url = "home/" + this.administrador!.usuarioId + "/administrador/crear-investigador";
    this._router.navigate([url]);
  }
  
  /**
   * Edita los datos de un investigador
   */
  gestionarInvestigador(): void{
    if(this.investigadorSelect){
      let url = "home/" + this.administrador!.usuarioId + "/administrador/gestionar-investigador/" + this.investigadorSelect!.usuarioId;
      this._router.navigate([url]);
    }
    else{
      //Muestra los errores cometidos por el usuario
      this.mostrarError("tableInvestigador","errorInvestigadores", "No ha seleccionado un investigador");
       //Oculta un error
       setTimeout( () => this.ocultarError("tableInvestigador","errorInvestigadores"), 10000);
    }
  }

  /**
   * De todos los investigadores se selecciona uno a la vez
   * @param investigador 
   */
  seleccionarInvestigador(investigador: ModeloUsuario): void{
    this.investigadorSelect = investigador;
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
