package com.backend.applicaiton_backend.logicanegocio.DTO;

import java.time.LocalDateTime;
import java.util.List;
import javax.persistence.Entity;

import com.backend.applicaiton_backend.infraestructura.modelo.ModeloImagen;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class UsuarioDto {

	private Long usuarioId;

	/**
	 * Nombre usuario
	 */
	private String nombre;

	/**
	 * Correo registro
	 */
	private String correo;

	/**
	 * Permisos de administrador o no
	 */
	private Boolean administrador;

	/**
	 * Fecha de creacion
	 */
	private LocalDateTime fechaCreacion;

	/**
	 * Habilitado para utilizar el sistema
	 */
	private Boolean habilitado;

	/**
	 * Imagenes agregadas por el usuario.
	 */
	private List<ModeloImagen> imagenes;

}
