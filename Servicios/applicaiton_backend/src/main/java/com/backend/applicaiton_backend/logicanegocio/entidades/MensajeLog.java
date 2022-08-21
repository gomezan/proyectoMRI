package com.backend.applicaiton_backend.logicanegocio.entidades;

import lombok.Getter;
import lombok.RequiredArgsConstructor;

/**
 * Enum que representa los mensajes de respuesta hacia la vista
 *
 * @author <a href="santiagoromero@javeriana.edu.co"> Santiago Romero </a>
 * @since 1.0.0
 */
@RequiredArgsConstructor
@Getter
public enum MensajeLog {


	/**
	 * error guardando usuario
	 */
	ERROR_GUARDANDO_USUARIO("Error mientras guarda el usuario {}, la excepcion fue: {}"),

	/**
	 * error al actualizar una imagen
	 */
	ERROR_PROCESAR_ESTADO("La imagen a actualizar no presenta el estado al cual debe ser actualizado"),

	/**
	 * la imagen se encuentra en procesamiento, en se puede cancelar
	 */
	ERROR_CANCELAR_PROCESAMIENTO("la imagen se encuentra en procesamiento, en se puede cancelar"),

	/**
	 * Usuario no encontrado
	 */
	IMAGEN_NO_EXISTE("imagen {} no encontrada, excepcion: {}"),


	/**
	 * Error trayendo imagenes por usuario
	 */
	IMAGENES_NO_EXISTENTES("problema trayendo imagenes"),

	/**
	 * Imagen actualizada
	 */
	IMAGEN_ACTUALIZADA("imagen {} actualizada"),



	/**
	 * Usuario no encontrado
	 */
	IMAGEN_NO_PERTENECE_USUARIO("imagen {} no pertenece al usuario {}, excepcion: {}"),

	/**
	 * Usuario no encontrado
	 */
	USUARIO_NO_EXISTE("Usuario {} no encontrado, excepcion: {}");

	/**
	 * llave para acceder al enum
	 */
	private String llave;


	/**
	 * Constructor of {@link MensajeRespuesta}
	 *
	 * @param llave to get the enum
	 */
	MensajeLog(final String llave) {
		this.llave = llave;
	}
}
