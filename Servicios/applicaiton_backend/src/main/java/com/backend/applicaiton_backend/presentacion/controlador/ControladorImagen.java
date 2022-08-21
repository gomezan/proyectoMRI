package com.backend.applicaiton_backend.presentacion.controlador;

import java.util.List;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import com.backend.applicaiton_backend.infraestructura.modelo.ModeloImagen;
import com.backend.applicaiton_backend.infraestructura.modelo.ModeloUsuario;
import com.backend.applicaiton_backend.logicanegocio.DTO.UsuarioDto;
import com.backend.applicaiton_backend.logicanegocio.casosuso.GestionaImagenCU;
import com.backend.applicaiton_backend.logicanegocio.casosuso.GestionaUsuarioCU;
import com.backend.applicaiton_backend.logicanegocio.entidades.Estado;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

/**
 * Controlador imagen
 *
 * @author <a href="santiagoromero@javeriana.edu.co"> Santiago Romero </a>
 * @since 1.0.0
 */
@Slf4j
@RestController
@RequiredArgsConstructor
@RequestMapping("/imagen")
public class ControladorImagen {

	/**
	 * Caso de uso gestionar imagen
	 */
	private final GestionaImagenCU gestionaImagenCU;

	/**
	 * Caso de uso gestionar usuario
	 */
	private final GestionaUsuarioCU gestionaUsuarioCU;


	/**
	 * Crea imagen
	 *
	 * @param  imagen {@link ModeloImagen}
	 */
	@PostMapping("/crear_imagen")
	public ResponseEntity<ModeloImagen> crearImagen(@RequestBody ModeloImagen imagen){
		imagen.setEstado(Estado.SUBIDO);
		return new ResponseEntity<>(gestionaImagenCU.crearImagen(imagen), HttpStatus.CREATED);
	}

	/**
	 * Cancelar procesamiento
	 *
	 * @param  imagenId {@link ModeloImagen}
	 */
	@PutMapping("/cancelar_procesamiento/{imagenId}")
	public ResponseEntity<ModeloImagen> cancelaProcesoImagen(@PathVariable Long imagenId){
		ModeloImagen imagen = gestionaImagenCU.obtenerImagen(imagenId);
		imagen.setEstado(Estado.CANCELADO);
		gestionaImagenCU.actualizarImagen(imagen);
		return new ResponseEntity<>(HttpStatus.OK);
	}

	/**
	 * Obtiene todas las imagenes con su informacion
	 *
	 * @param  usuarioId {@link ModeloUsuario}
	 */
	@GetMapping("/obtener_imagenes_por_usuario/{usuarioId}")
	public ResponseEntity<List<ModeloImagen>> obtenerImagenesPorUsuario(@PathVariable Long usuarioId){
		ModeloUsuario usuario = gestionaUsuarioCU.encontrarUsuarioPorIdM(usuarioId);
		List<ModeloImagen> imagenes = gestionaImagenCU.obtenerImagenesPorUsuario(usuario);
		return new ResponseEntity<>(imagenes,HttpStatus.OK);
	}

	/**
	 * Obtiene la siguiente imagen para procesar
	 *
	 */
	@GetMapping("/obtener_siguiente_imagen_a_procesar")
	public ResponseEntity<ModeloImagen> obtenerSiguienteImagen(){
		ModeloImagen imagen = gestionaImagenCU.obtenerSiguienteImagen();
		return new ResponseEntity<>(imagen,HttpStatus.OK);
	}

	/**
	 * Actualiza el estado a imagen descargada
	 *
	 * @param  imagenId {@link ModeloImagen}
	 */
	@PutMapping("/descargar_imagen/{imagenId}")
	public ResponseEntity<ModeloImagen> descargarImagen(@PathVariable Long imagenId){
		ModeloImagen imagen = gestionaImagenCU.obtenerImagen(imagenId);
		imagen.setEstado(Estado.DESCARGADO);
		gestionaImagenCU.actualizarImagen(imagen);
		return new ResponseEntity<>(HttpStatus.OK);
	}

}
