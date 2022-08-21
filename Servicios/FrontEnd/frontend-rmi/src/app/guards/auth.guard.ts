import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import {
  ActivatedRouteSnapshot,
  CanActivate,
  RouterStateSnapshot,
} from '@angular/router';
import { Observable, of } from 'rxjs';
import { LoginService } from '../shared/login.service';
import {take, map, tap} from 'rxjs/operators';

//Permite que el acceso a las rutas si el usuario está autenticado
@Injectable()
export class AuthGuard implements CanActivate {
  constructor(private authService: LoginService, private _router: Router) {}
  canActivate(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot
  ): boolean | Observable<boolean> | Promise<boolean> {
    //Llama al servicio de login y obtiene el estado de la autenticación y los datos del usuario
    const isAuth = this.authService.getIsAuth();
    const user = this.authService.getAuthData();
    if (!isAuth) {
      if(user){
        /**
         * Si el usuario no está autenticado pero hay datos guardados en SessionStorage lo redirige a su home
         * esto evita que se pierda la sesión a la hora de refrescar la página
         */
        this.authService.setIsAuth(true);
        this._router.navigate(['/home', user['token'], user['rol']]);
        return true
      }
      else{
        //Si el usuario no está autenticado y no hay nada guardado en SessionStorage, regresa a Login
        this._router.navigate(['/login']);
        return false
      }
    }
    else{
      //Si está autenticado puede avanzar a través de la navegación
      return true;
    }
  }
}
