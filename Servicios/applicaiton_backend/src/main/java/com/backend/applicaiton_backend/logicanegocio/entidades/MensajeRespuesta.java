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
public enum MensajeRespuesta {
	/**
	 * Usuario ya existente
	 */
	USUARIO_YA_EXISTE("Usuario ya existente"),

	/**
	 * Error guardando informacion
	 */
	ERROR_GUARDANDO_INFO("Error guardando informacion"),

	/**
	 * Clave erronea
	 */
	CLAVE_ERRONEA("Clave erronea"),

	/**
	 * Usuario no habilitado, comuniquese con el administrador
	 */
	USUARIO_NO_HABILITADO("Usuario no habilitado, comuniquese con el administrador"),

	/**
	 * la imagen se encuentra en procesamiento, en se puede cancelar
	 */
	ERROR_CANCELAR_PROCESAMIENTO("la imagen se encuentra en procesamiento, en se puede cancelar"),


	/**
	 * Inconsistencia de estados
	 */
	ERROR_DE_ESTADO("El estado no puede ser procesado"),

	/**
	 * Usuario no encontrado
	 */
	IMAGEN_NO_ENCONTRADA("Imagen no encontrada"),

	/**
	 * Usuario no encontrado
	 */
	USUARIO_NO_ENCONTRADO("Usuario no encontrado");


	/**
	 * llave para acceder al enum
	 */
	private String llave;


	/**
	 * Constructor of {@link MensajeRespuesta}
	 *
	 * @param llave to get the enum
	 */
	MensajeRespuesta(final String llave) {
		this.llave = llave;
	}
}
