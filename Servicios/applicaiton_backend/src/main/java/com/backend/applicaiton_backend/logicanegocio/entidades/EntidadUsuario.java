package com.backend.applicaiton_backend.logicanegocio.entidades;

import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.extern.slf4j.Slf4j;

/**
 * DTO de la clase usuario.
 *
 * @author <a href="santiagoromero@javeriana.edu.co"> Santiago Romero </a>
 * @since 1.0.0
 */
@Data
@Slf4j
@NoArgsConstructor
public class EntidadUsuario {

	// -----------------------------------------------------------------------------------------------------------------
	// Atributos
	// -----------------------------------------------------------------------------------------------------------------

	/**
	 * Usuario id.
	 */
	private Long id;

	/**
	 * Nombre usuario
	 */
	private String nombre;

	/**
	 * Correo registro
	 */
	private String correo;

	/**
	 * Clave
	 */
	private String clave;

	/**
	 * Permisos de administrador o no
	 */
	private Boolean administrador;

	/**
	 * Habilitado para utilizar el sistema
	 */
	private Boolean habilitado;
}
