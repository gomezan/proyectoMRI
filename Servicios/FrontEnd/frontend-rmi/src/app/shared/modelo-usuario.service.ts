import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { ModeloUsuario } from '../model/modelo-usuario';

@Injectable({
  providedIn: 'root'
})
export class ModeloUsuarioService {

  constructor(private http: HttpClient) { }

  /**
   * Guarda un nuevo usuario en el sistema
   * @param usuario 
   * @returns 
   */
  postCrearUsuario(usuario: ModeloUsuario): Observable<ModeloUsuario>{
    return this.http.post<ModeloUsuario>(environment.URL_BACKEND_BASE + "/usuario/crear_usuario", usuario,
    {
      withCredentials: true
    });
  }

  /**
   * Actualiza los datos de un usuario
   * @param usuario 
   * @returns 
   */
  putAdmin(usuario: ModeloUsuario): Observable<ModeloUsuario>{
    return this.http.put<ModeloUsuario>(environment.URL_BACKEND_BASE + "/usuario/actualizar_usuario_admin", usuario,
    {
      withCredentials: true
    });
  }

  /**
   * Actualiza la clave de un suaurio
   * @param usuario 
   * @returns 
   */
  putClaveUsuario(usuario: ModeloUsuario): Observable<ModeloUsuario>{
    return this.http.put<ModeloUsuario>(environment.URL_BACKEND_BASE + "/usuario/actualizar_clave", usuario,
    {
      withCredentials: true
    });
  }

  /**
   * Función que encuentra a un usuario utilizando su clave (contraseña) y correo
   * Es especialmente útil a la hora de iniciar sesión
   * @param usuario 
   * @returns 
   */
  postLogIn(usuario: ModeloUsuario): Observable<ModeloUsuario>{
    return this.http.post<ModeloUsuario>(environment.URL_BACKEND_BASE + "/usuario/iniciar_sesion", usuario,
    {
      withCredentials: true
    });
  }

  /**
   * Encuentra un usuario por un id
   * @param usuarioId identificador de un usuario
   * @returns 
   */
  findUsuarioById(usuarioId: number): Observable<ModeloUsuario>{
    return this.http.get<ModeloUsuario>(environment.URL_BACKEND_BASE + "/usuario/encontrar_usuario/" + usuarioId,
    {
      withCredentials: true
    });
  }

  /**
   * Encuentra a todos los investigadores registrados en el sistema
   * @returns 
   */
  findAllInvestigadores(): Observable<ModeloUsuario[]>{
    return this.http.get<ModeloUsuario[]>(environment.URL_BACKEND_BASE + "/usuario/obtener_usuarios_diferentes_al_admin",
    {
      withCredentials: true
    });
  }
}
