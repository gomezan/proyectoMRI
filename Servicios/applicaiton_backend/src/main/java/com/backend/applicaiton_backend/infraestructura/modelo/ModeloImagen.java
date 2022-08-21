package com.backend.applicaiton_backend.infraestructura.modelo;

import java.time.LocalDateTime;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.EnumType;
import javax.persistence.Enumerated;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.Table;

import org.hibernate.annotations.DynamicUpdate;
import org.hibernate.annotations.Type;
import org.hibernate.annotations.TypeDef;
import com.backend.applicaiton_backend.logicanegocio.entidades.Estado;
import com.fasterxml.jackson.annotation.JsonBackReference;
import com.vladmihalcea.hibernate.type.json.JsonBinaryType;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.NoArgsConstructor;
import lombok.ToString;

/**
 * Modelado de la imagen en la base de datos.
 *
 * @author <a href="santiagoromero@javeriana.edu.co"> Santiago Romero </a>
 * @since 1.0.0
 */
@Data
@Entity
@NoArgsConstructor
@AllArgsConstructor
@DynamicUpdate
@Table(name = "imagen")
@TypeDef(name = "jsonb", typeClass = JsonBinaryType.class)
public class ModeloImagen {

	/**
	 * Usuario id.
	 */
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	@Column(name = "imagen_id", updatable = false)
	private Long imagenId;

	/**
	 * Usuario id que subio la imagen.
	 */
	@JsonBackReference
	@ToString.Exclude
	@EqualsAndHashCode.Exclude
	@ManyToOne(fetch = FetchType.LAZY)
	@JoinColumn(name = "usuario_id")
	private ModeloUsuario usuario;

	/**
	 * Nombre imagen
	 */
	@Column(name = "nombre")
	private String nombre;

	/**
	 * Observacion (descripcion de la imagen)
	 */
	@Column(name = "observacion")
	private String observacion;

	/**
	 * Estado de la imagen
	 */
	@Column(name = "estado")
	@Enumerated(EnumType.STRING)
	private Estado estado;

	/**
	 * caracteristicas de la imagen original
	 */
	@Column(name = "descripcion_original")
	@Type(type = "jsonb")
	private String descripcionOriginal;

	/**
	 * ruta de la imagen inicial
	 */
	@Column(name = "ruta_original")
	private String rutaOriginal;

	/**
	 * Fecha cuando se carga la imagen
	 */
	@Column(name = "fecha_inicial")
	private LocalDateTime fechaInicial;

	/**
	 * Fecha cuando se elimina la imagen
	 */
	@Column(name = "fecha_eliminacion")
	private LocalDateTime fechaEliminacion;

	/**
	 * caracteristicas de la imagen procesada
	 */
	@Column(name = "descripcion_procesada")
	@Type(type = "jsonb")
	private String descripcionProcesada;

	/**
	 * ruta de la imagen procesada
	 */
	@Column(name = "ruta_procesada")
	private String rutaProcesada;

	/**
	 * Fecha cuando se procesa la imagen
	 */
	@Column(name = "fecha_procesamiento")
	private LocalDateTime fechaProcesamiento;

}
