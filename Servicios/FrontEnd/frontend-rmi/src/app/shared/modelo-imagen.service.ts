import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { ModeloImagen } from '../model/modelo-imagen';

@Injectable({
  providedIn: 'root'
})
export class ModeloImagenService {

  constructor(private http: HttpClient) { }

  /**
   * Guarda los datos de una nueva imagen
   * @param imagen 
   * @returns 
   */
  postImagen(imagen: ModeloImagen): Observable<ModeloImagen>{
    return this.http.post<ModeloImagen>(environment.URL_BACKEND_BASE + "/imagen/crear_imagen", imagen,
    {
      withCredentials: true
    });
  }

  /**
   * Cancela el procesamiento de una imagen
   * @param imagenId identificador de una imagen
   * @returns 
   */
  putImagen(imagenId: number): Observable<ModeloImagen>{
    return this.http.put<ModeloImagen>(environment.URL_BACKEND_BASE + "/imagen/cancelar_procesamiento/" + imagenId, 
    {
      withCredentials: true
    });
  }

  /**
   * Cambia el estado de una imagen a DESCARGADO
   * @param imagenId identificador de una imagen
   * @returns 
   */
  putDescargarImagen(imagenId: number): Observable<ModeloImagen>{
    return this.http.put<ModeloImagen>(environment.URL_BACKEND_BASE + "/imagen/descargar_imagen/" + imagenId, 
    {
      withCredentials: true
    });
  }

  /**
   * Retorna todos los datos de todas las imagenes de un usuario determinado
   * @param usuarioId identificador de un usuario
   * @returns 
   */
  findImagenesByUsuarioId(usuarioId: number): Observable<ModeloImagen[]>{
    return this.http.get<ModeloImagen[]>(environment.URL_BACKEND_BASE + "/imagen/obtener_imagenes_por_usuario/" + usuarioId,
    {
      withCredentials: true
    });
  }
  
  /**
   * Obtiene la siguiente imagen que está en cola para ser procesada
   * @returns 
   */
  findImagenSiguiente(): Observable<ModeloImagen>{
    return this.http.get<ModeloImagen>(environment.URL_BACKEND_BASE + "/imagen/obtener_siguiente_imagen_a_procesar",
    {
      withCredentials: true
    });
  }
}
