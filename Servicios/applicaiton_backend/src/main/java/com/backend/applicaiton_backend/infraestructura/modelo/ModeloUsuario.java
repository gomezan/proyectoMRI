package com.backend.applicaiton_backend.infraestructura.modelo;

import java.time.LocalDateTime;
import java.util.List;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.OneToMany;
import javax.persistence.Table;

import org.hibernate.annotations.DynamicUpdate;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonManagedReference;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.Singular;

/**
 * Modelado del usuario en la base de datos.
 *
 * @author <a href="santiagoromero@javeriana.edu.co"> Santiago Romero </a>
 * @since 1.0.0
 */
@Data
@Entity
@NoArgsConstructor
@AllArgsConstructor
@DynamicUpdate
@Table(name = "usuario")
public class ModeloUsuario {

	// -----------------------------------------------------------------------------------------------------------------
	// Atributos
	// -----------------------------------------------------------------------------------------------------------------

	/**
	 * Usuario id.
	 */
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	@Column(name = "usuario_id", updatable = false)
	private Long usuarioId;

	/**
	 * Nombre usuario
	 */
	@Column(name = "nombre")
	private String nombre;

	/**
	 * Correo registro
	 */
	@Column(name = "correo")
	private String correo;

	/**
	 * Clave
	 */
	@Column(name = "clave")
	private String clave;

	/**
	 * Permisos de administrador o no
	 */
	@Column(name = "administrador", columnDefinition = "false")
	private Boolean administrador;

	/**
	 * Fecha de creacion
	 */
	@Column(name = "fecha_creacion")
	private LocalDateTime fechaCreacion;

	/**
	 * Habilitado para utilizar el sistema
	 */
	@Column(name = "habilitado", columnDefinition = "true")
	private Boolean habilitado;

	/**
	 * Imagenes agregadas por el usuario.
	 */
	@Singular("imagenes")
	@JsonManagedReference
	@OneToMany(fetch = FetchType.LAZY,
			cascade = CascadeType.ALL,
			mappedBy = "usuario")
	private List<ModeloImagen> imagenes;

}
