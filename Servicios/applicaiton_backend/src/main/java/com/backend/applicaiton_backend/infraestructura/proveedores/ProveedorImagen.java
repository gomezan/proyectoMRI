package com.backend.applicaiton_backend.infraestructura.proveedores;

import java.util.List;
import java.util.Optional;

import org.springframework.dao.RecoverableDataAccessException;
import com.backend.applicaiton_backend.infraestructura.modelo.ModeloImagen;
import com.backend.applicaiton_backend.infraestructura.modelo.ModeloUsuario;
import com.backend.applicaiton_backend.infraestructura.repositorio.RepositorioImagen;
import com.backend.applicaiton_backend.logicanegocio.entidades.MensajeLog;
import com.backend.applicaiton_backend.logicanegocio.entidades.MensajeRespuesta;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

/**
 * Se encarga de hacer los llamados al repositorio hibernate de la imagen.
 *
 * @author <a href="santiagoromero@javeriana.edu.co"> Santiago Romero </a>
 * @since 1.0.0
 */

@Slf4j
@RequiredArgsConstructor
public class ProveedorImagen {

	/**
	 * Repositorio Imagen
	 */
	private final RepositorioImagen repositorio;

	/**
	 * Guarda/Crea un {@link ModeloImagen}
	 *
	 * @param modeloImagen una instancia de {@linkplain ModeloImagen}.
	 */
	public ModeloImagen crearGuardarImagen(ModeloImagen modeloImagen){
		try{
			return repositorio.save(modeloImagen);
		}catch(Exception e){
			log.error(MensajeLog.ERROR_GUARDANDO_USUARIO.getLlave(), modeloImagen, e);
			throw new RecoverableDataAccessException(MensajeRespuesta.ERROR_GUARDANDO_INFO.getLlave(), e);
		}
	}

	/**
	 * busca un {@link ModeloImagen} en db por id
	 *
	 * @param modeloImagenId Id del {@linkplain ModeloImagen}.
	 * @return un {@link Optional <ModeloUsuario>}
	 */
	public Optional<ModeloImagen> encontrarImagenPorId(Long modeloImagenId){
		try{
			return repositorio.findById(modeloImagenId);
		}catch(Exception e){
			log.warn(MensajeLog.IMAGEN_NO_EXISTE.getLlave(),modeloImagenId,e);
			return Optional.empty();
		}
	}

	/**
	 * busca imagenes {@link ModeloImagen} en db por id de usuario
	 *
	 * @param modeloUsuario Id del {@linkplain ModeloUsuario}.
	 * @return un {@link Optional <ModeloUsuario>}
	 */
	public List<ModeloImagen> encontrarImagenesPorUsuarioId(ModeloUsuario modeloUsuario){

			return repositorio.findAllByUsuario(modeloUsuario);

	}

	/**
	 * busca imagenes {@link ModeloImagen} en db por id de usuario
	 *
	 * @return un {@link Optional <ModeloUsuario>}
	 */
	public ModeloImagen obtenerSiguienteImagen(){

		return repositorio.obtenerSiguienteImagen();

	}

	/**
	 * Cambia el estado de las imagenes a eliminado
	 *
	 */
	public void eliminarImagenes(){

		repositorio.eliminarImagenes();

	}

	/**
	 * busca un {@link ModeloImagen} en db por id
	 *
	 * @param modeloImagenId Id del {@linkplain ModeloImagen}
	 * @param usuarioId Id del {@linkplain ModeloUsuario}
	 * @return un {@link Optional <ModeloUsuario>}

	public Optional<ModeloImagen> encontrarImagenPorIdYUsuarioId(Long modeloImagenId, Long usuarioId){
		try{
			return repositorio.findByIdAndUsuario(modeloImagenId, usuarioId);
		}catch(Exception e){
			log.warn(MensajeLog.IMAGEN_NO_PERTENECE_USUARIO.getLlave(),modeloImagenId,usuarioId,e);
			return Optional.empty();
		}
	}*/
}
