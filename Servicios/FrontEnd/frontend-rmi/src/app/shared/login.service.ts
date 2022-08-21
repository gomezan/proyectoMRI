import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { environment } from 'src/environments/environment';
import { ModeloUsuario } from '../model/modelo-usuario';
import { map } from 'rxjs/operators';

/**
 * Se encarga de la parte de inicio de sesión
 */
@Injectable({
  providedIn: 'root'
})
export class LoginService {

  //Establece si el usuario está autenticado
  private isAuth = false;
  constructor(private http: HttpClient) {}

  /**
   * Retorna el estado de autenticación
   */
  getIsAuth() {
    return this.isAuth;
  }

  /**
   * Modifica el estado de autenticación
   * @param estado 
   */
  setIsAuth(estado: boolean){
    this.isAuth = estado;
  }

  /**
   * Servicio de inicio de sesión
   * @param usuario que inicia sesión
   * @returns 
   */
  login(usuario: ModeloUsuario): Observable<ModeloUsuario> {
    //Establece los Headers HTTP
    const formHeaders = new HttpHeaders();
    formHeaders.append('Content-Type', 'application/x-www-form-urlencoded');
    //Pasa por parametro el correo y la clave ingresada
    const formParams = new HttpParams()
      .set('username', usuario.correo)
      .set('password', usuario.clave);
    return this.http
      .post<ModeloUsuario>(environment.URL_BACKEND_BASE + "/usuario/iniciar_sesion", usuario, {
        headers: formHeaders,
        params: formParams,
        withCredentials: true,
      });
  }

  /**
   * Salva los datos en SessionStorage
   * @param token id del usuario
   * @param rol del usuario
   */
  saveAuthData(token: number, rol: string) {
    let str = token.toString();
    sessionStorage.setItem('token', str);
    sessionStorage.setItem('rol', rol);
  }

  /**
   * Retorna los datos de autenticación
   * @returns 
   */
  getAuthData() {
    const token = sessionStorage.getItem('token');
    const rol = sessionStorage.getItem('rol');

    if (!token) {
      return;
    }
    return {
      message: 'Este es el usuario',
      token,
      rol
    };
  }

  /**
   * Limpia los datos de autenticación
   */
  clearAuthData() {
    sessionStorage.removeItem('token');
    sessionStorage.removeItem('rol');
  }

  /**
   * Cierra la sesión del usuario
   */
  logout() {
    this.isAuth = false;
      this.clearAuthData();
  }
}
