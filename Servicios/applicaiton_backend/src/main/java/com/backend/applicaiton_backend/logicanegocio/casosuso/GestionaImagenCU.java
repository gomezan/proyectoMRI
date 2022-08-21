package com.backend.applicaiton_backend.logicanegocio.casosuso;

import java.text.NumberFormat;
import java.text.ParseException;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.List;
import java.util.Map;
import java.util.Optional;

import org.springframework.http.HttpStatus;
import org.springframework.web.server.ResponseStatusException;
import com.backend.applicaiton_backend.infraestructura.modelo.ModeloImagen;
import com.backend.applicaiton_backend.infraestructura.modelo.ModeloUsuario;
import com.backend.applicaiton_backend.infraestructura.proveedores.ProveedorImagen;
import com.backend.applicaiton_backend.logicanegocio.entidades.Estado;
import com.backend.applicaiton_backend.logicanegocio.entidades.MensajeRespuesta;
import lombok.NonNull;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

import static com.backend.applicaiton_backend.logicanegocio.entidades.Estado.PROCESANDO;
import static com.backend.applicaiton_backend.logicanegocio.entidades.MensajeLog.ERROR_CANCELAR_PROCESAMIENTO;
import static com.backend.applicaiton_backend.logicanegocio.entidades.MensajeLog.ERROR_PROCESAR_ESTADO;
import static com.backend.applicaiton_backend.logicanegocio.entidades.MensajeLog.IMAGEN_ACTUALIZADA;
import static java.util.Objects.isNull;

/**
 * Logica de toda la gestion de la imagen.
 *
 * @author <a href="santiagoromero@javeriana.edu.co"> Santiago Romero </a>
 * @since 1.0.0
 */

@Slf4j
@RequiredArgsConstructor
public class GestionaImagenCU {

	/**
	 * proveedor de datos de imagen
	 */
	private final ProveedorImagen proveedor;

	/**
	 * Crea una imagen
	 *
	 * @param modeloImagen {@link ModeloImagen}
	 * @return {@link ModeloUsuario} creado
	 */
	public ModeloImagen crearImagen(ModeloImagen modeloImagen) {

		modeloImagen.setFechaInicial(LocalDateTime.now());
		modeloImagen.setFechaEliminacion(LocalDateTime.now().plusDays(3));
		modeloImagen.setEstado(Estado.SUBIDO);
		return proveedor.crearGuardarImagen(modeloImagen);
	}

	/**
	 * Cambia el estado de las imagenes que ya deban estar eliminadas hasta la fecha
	 *
	 */
	public void eliminarImagenes() {
		proveedor.eliminarImagenes();

	}

	/**
	 * Encontrar Imagen por id y por usuario
	 *
	 * @param imagenId {@link ModeloImagen}
	 *
	 * @return {@link ModeloUsuario}
	 */
	public ModeloImagen obtenerImagen(Long imagenId){

		Optional<ModeloImagen> imagen = proveedor.encontrarImagenPorId(imagenId);
		if (!imagen.isPresent()) {
			throw new ResponseStatusException(HttpStatus.NOT_FOUND, MensajeRespuesta.IMAGEN_NO_ENCONTRADA.getLlave());
		}

		return imagen.get();
	}

	/**
	 * Encontrar Imagen por id y por usuario
	 *
	 * @param modeloUsuario {@link ModeloUsuario}
	 *
	 * @return <list> {@link ModeloImagen}
	 */
	public List<ModeloImagen> obtenerImagenesPorUsuario(ModeloUsuario modeloUsuario){
		List<ModeloImagen> imagenes = proveedor.encontrarImagenesPorUsuarioId(modeloUsuario);

		return imagenes;
	}

	/**
	 * Obtiene la siguiente imagen a procesar y actualiza el estado
	 *
	 * @return  {@link ModeloImagen}
	 */
	public ModeloImagen obtenerSiguienteImagen(){
		ModeloImagen imagen = proveedor.obtenerSiguienteImagen();
		if(imagen == null){
			throw new ResponseStatusException(HttpStatus.NOT_FOUND);
		}
		imagen.setEstado(PROCESANDO);
		proveedor.crearGuardarImagen(imagen);
		return imagen;
	}

	/**
	 * Actualiza la imagen
	 *
	 * @param modeloImagen {@link ModeloImagen}
	 *
	 */
	public void actualizarImagen(ModeloImagen modeloImagen){

		Optional<ModeloImagen> imagen = proveedor.encontrarImagenPorId(modeloImagen.getImagenId());
		if (!imagen.isPresent()) {
			throw new ResponseStatusException(HttpStatus.NOT_FOUND, MensajeRespuesta.IMAGEN_NO_ENCONTRADA.getLlave());
		}
		proveedor.crearGuardarImagen(validacionActualizacionImagen(modeloImagen,imagen.get()));

	}

	/**
	 * Actualiza proveniente de la cola
	 *
	 * @param mapaImagen {@link ModeloImagen}
	 *
	 */
	public void actualizarImagenCola(Map<String, Object> mapaImagen) {

		Optional<ModeloImagen> imagenOp = proveedor.encontrarImagenPorId( (long)Double.parseDouble(mapaImagen.get("imagenId").toString()) );
		ModeloImagen  imagen = imagenOp.get();
		imagen.setEstado( Estado.valueOf(mapaImagen.get("estado").toString()));
		DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
		LocalDateTime dateTime = LocalDateTime.parse(mapaImagen.get("fechaProcesamiento").toString(), formatter);
		imagen.setFechaProcesamiento(dateTime);
		imagen.setRutaProcesada((String) mapaImagen.get("rutaProcesada"));
		imagen.setDescripcionProcesada((String) mapaImagen.get("descripcionProcesada"));
		log.info("imagen {} actualizada",imagen.toString());
		proveedor.crearGuardarImagen(imagen);

	}

	public void actualizarImagenCola(ModeloImagen imagenEntrada) {

		Optional<ModeloImagen> imagenOp = proveedor.encontrarImagenPorId( imagenEntrada.getImagenId());
		ModeloImagen imagen = imagenOp.get();
		imagen.setEstado( imagenEntrada.getEstado());
		LocalDateTime dateTime = imagenEntrada.getFechaProcesamiento();
		imagen.setFechaProcesamiento(dateTime);
		imagen.setRutaProcesada( imagenEntrada.getRutaProcesada());
		imagen.setDescripcionProcesada( imagenEntrada.getDescripcionProcesada());
		log.info("imagen {} actualizada",imagen.toString());
		proveedor.crearGuardarImagen(imagen);

	}


	private ModeloImagen validacionActualizacionImagen(ModeloImagen imagenEntrada, ModeloImagen imagenActualizar){

		if(isNull(imagenEntrada.getEstado())){
			log.error(ERROR_PROCESAR_ESTADO.getLlave());
			throw new ResponseStatusException(HttpStatus.CONFLICT, MensajeRespuesta.ERROR_DE_ESTADO.getLlave());
		}

		imagenActualizar.setEstado(imagenEntrada.getEstado());
		if (PROCESANDO.equals(imagenEntrada.getEstado())) {
			imagenActualizar.setFechaProcesamiento(LocalDateTime.now());
		}
		if (Estado.CANCELADO.equals(imagenEntrada.getEstado())) {
			if(PROCESANDO.equals(imagenActualizar.getEstado())){
				log.warn(ERROR_CANCELAR_PROCESAMIENTO.getLlave());
				throw new ResponseStatusException(HttpStatus.CONFLICT, MensajeRespuesta.ERROR_CANCELAR_PROCESAMIENTO.getLlave());
			}
			imagenActualizar.setEstado(Estado.CANCELADO);
		}
		if(!isNull(imagenEntrada.getDescripcionProcesada())){
			imagenActualizar.setDescripcionProcesada(imagenEntrada.getDescripcionProcesada());
		}

		log.info(IMAGEN_ACTUALIZADA.getLlave(), imagenActualizar.getImagenId() );
		return imagenActualizar;
	}


}
