package com.backend.applicaiton_backend.infraestructura.proveedores;

import java.util.List;
import java.util.Optional;

import org.springframework.dao.RecoverableDataAccessException;
import com.backend.applicaiton_backend.infraestructura.modelo.ModeloUsuario;
import com.backend.applicaiton_backend.infraestructura.repositorio.RepositorioUsuario;
import com.backend.applicaiton_backend.logicanegocio.entidades.MensajeLog;
import com.backend.applicaiton_backend.logicanegocio.entidades.MensajeRespuesta;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

/**
 * Se encarga de hacer los llamados al repositorio hibernate del usuario.
 *
 * @author <a href="santiagoromero@javeriana.edu.co"> Santiago Romero </a>
 * @since 1.0.0
 */
@Slf4j
@RequiredArgsConstructor
public class ProveedorUsuario {

	/**
	 * Repositorio usuario
	 */
	private final RepositorioUsuario repositorio;

	/**
	 * Guarda/Creaa un {@link ModeloUsuario}
	 *
	 * @param modeloUsuario una instancia de {@linkplain ModeloUsuario}.
	 */
	public ModeloUsuario crearGuardarUsuario(ModeloUsuario modeloUsuario){
		try{
			return repositorio.save(modeloUsuario);
		}catch(Exception e){
			log.error(MensajeLog.ERROR_GUARDANDO_USUARIO.getLlave(),modeloUsuario,e);
			throw new RecoverableDataAccessException(MensajeRespuesta.ERROR_GUARDANDO_INFO.getLlave(), e);
		}
	}

	/**
	 * busca un {@link ModeloUsuario} en db por correo
	 *
	 * @param modeloUsuario una instancia de {@linkplain ModeloUsuario}.
	 * @return un {@link Optional<ModeloUsuario>}
	 */
	public Optional<ModeloUsuario> encontrarUsuarioPorCorreo(ModeloUsuario modeloUsuario){
		try{
			return repositorio.findByCorreo(modeloUsuario.getCorreo());
		}catch(Exception e){
			log.warn(MensajeLog.USUARIO_NO_EXISTE.getLlave(), modeloUsuario, e);
			return Optional.empty();
		}
	}

	/**
	 * busca un {@link ModeloUsuario} en db por correo
	 *
	 * @param correo de un usuario.
	 * @return un {@link Optional<ModeloUsuario>}
	 */
	public Optional<ModeloUsuario> encontrarUsuarioPorCorreo(String correo){
		try{
			return repositorio.findByCorreo(correo);
		}catch(Exception e){
			log.warn(MensajeLog.USUARIO_NO_EXISTE.getLlave(), correo, e);
			return Optional.empty();
		}
	}

	/**
	 * busca un {@link ModeloUsuario} en db por id
	 *
	 * @param modeloUsuario una instancia de {@linkplain ModeloUsuario}.
	 * @return un {@link Optional<ModeloUsuario>}
	 */
	public Optional<ModeloUsuario> encontrarUsuarioPorId(ModeloUsuario modeloUsuario){
		try{
			return repositorio.findById(modeloUsuario.getUsuarioId());
		}catch(Exception e){
			log.warn(MensajeLog.USUARIO_NO_EXISTE.getLlave(),modeloUsuario,e);
			return Optional.empty();
		}
	}

	/**
	 * busca un {@link ModeloUsuario} en db por id
	 *
	 * @param modeloUsuarioId Id del {@linkplain ModeloUsuario}.
	 * @return un {@link Optional<ModeloUsuario>}
	 */
	public Optional<ModeloUsuario> encontrarUsuarioPorId(Long modeloUsuarioId){
		try{
			return repositorio.findById(modeloUsuarioId);
		}catch(Exception e){
			log.warn(MensajeLog.USUARIO_NO_EXISTE.getLlave(),modeloUsuarioId,e);
			return Optional.empty();
		}
	}

	/**
	 * busca usuarios {@link ModeloUsuario} diferentes
	 *
	 * @return un {@linkList<ModeloUsuario>}
	 */
	public List<ModeloUsuario> obtenerUsuarios() {

		return repositorio.encontrarUsuariosDiferentesAdmin();
	}


}
