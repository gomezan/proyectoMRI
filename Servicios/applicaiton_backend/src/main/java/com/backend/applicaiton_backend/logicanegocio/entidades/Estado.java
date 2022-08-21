package com.backend.applicaiton_backend.logicanegocio.entidades;

/**
 * Enum que representa el estado de una imagen agregada por un usuario
 *
 * @author <a href="santiagoromero@javeriana.edu.co"> Santiago Romero </a>
 * @since 1.0.0
 */
public enum Estado {

	SUBIDO,
	/**
	 Se presenta cuando el sistema del modelo inicie a procesar la imagen
	 */
	PROCESANDO,
	/**
	 se presenta cuando la imagen ya haya sido procesada exitosamente
	 */
	PROCESADO,
	/**
	 Se presenta cuando la imagen ha sido descargada (es valido aclarar que este estado solo se observara entre los
	 dias que la imagen haya sido descargada y no se encuentre eliminada del sistema de archivos)
	 */
	DESCARGADO,
	/**
	 Se presenta cuando La imagen ha sido eliminada del sistema de archivos
	 */
	ELIMINADO,
	/**
	 Se presenta cuando hay un error en el procesamiento de la imagen
	 */
	ERROR,
	/**
	Se presenta cuando la imagen no fue encontrada en el sistema de archivos
	 */
	NO_ENCONTRADO,
	/**
	 Se presenta cuando el usuario desea cancelar el procesamiento de la imagen cuando se encuentre en la cola de procesamiento
	 */
	CANCELADO

}


