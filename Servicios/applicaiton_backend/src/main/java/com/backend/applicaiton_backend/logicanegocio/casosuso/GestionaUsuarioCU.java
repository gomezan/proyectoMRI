package com.backend.applicaiton_backend.logicanegocio.casosuso;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import org.springframework.http.HttpStatus;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.web.server.ResponseStatusException;
import com.backend.applicaiton_backend.infraestructura.modelo.ModeloUsuario;
import com.backend.applicaiton_backend.infraestructura.proveedores.ProveedorUsuario;
import com.backend.applicaiton_backend.logicanegocio.DTO.UsuarioMapper;
import com.backend.applicaiton_backend.logicanegocio.DTO.UsuarioDto;
import com.backend.applicaiton_backend.logicanegocio.entidades.MensajeRespuesta;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

import static java.util.Objects.isNull;

/**
 * Logica de toda la gestion del usuario.
 *
 * @author <a href="santiagoromero@javeriana.edu.co"> Santiago Romero </a>
 * @since 1.0.0
 */
@Slf4j
@RequiredArgsConstructor
public class GestionaUsuarioCU {

	/**
	 * proveedor de datos de usuario
	 */
	private final ProveedorUsuario proveedor;

	BCryptPasswordEncoder encoder =new BCryptPasswordEncoder();

	/**
	 * Crea un  usuario
	 *
	 * @param modeloUsuario {@link ModeloUsuario}
	 * @return {@link UsuarioDto} creado
	 */
	public UsuarioDto crearUsuario(ModeloUsuario modeloUsuario) {

		Optional<ModeloUsuario> usuario = proveedor.encontrarUsuarioPorCorreo(modeloUsuario);

		if (usuario.isPresent()) {
			throw new ResponseStatusException(HttpStatus.CONFLICT, MensajeRespuesta.USUARIO_YA_EXISTE.getLlave());
		}
		modeloUsuario.setFechaCreacion(LocalDateTime.now());
		modeloUsuario.setClave(encoder.encode(modeloUsuario.getClave()));
		return UsuarioMapper.convertirUsuarioADto(proveedor.crearGuardarUsuario(modeloUsuario)) ;
	}

	/**
	 * Actualiza un  usuario por el administrador
	 *
	 * @param modeloUsuario {@link ModeloUsuario}
	 * @return {@link UsuarioDto} Actualizado
	 */
	public UsuarioDto actualizarUsuarioPorAdmin(final ModeloUsuario modeloUsuario) {

		Optional<ModeloUsuario> usuario = proveedor.encontrarUsuarioPorId(modeloUsuario);

		if (!usuario.isPresent()) {
			throw new ResponseStatusException(HttpStatus.NOT_FOUND, MensajeRespuesta.USUARIO_NO_ENCONTRADO.getLlave());
		}
		return UsuarioMapper.convertirUsuarioADto(proveedor.crearGuardarUsuario(validacionActualizarUsuarioPorAdmin(modeloUsuario, usuario.get())));
	}

	/**
	 * Actualiza un la clave por el usuario
	 *
	 * @param modeloUsuario {@link ModeloUsuario}
	 * @return {@link UsuarioDto} Actualizado
	 */
	public UsuarioDto actualizarClaveUsuario(final ModeloUsuario modeloUsuario) {

		Optional<ModeloUsuario> usuario = proveedor.encontrarUsuarioPorId(modeloUsuario);

		if (!usuario.isPresent()) {
			throw new ResponseStatusException(HttpStatus.NOT_FOUND, MensajeRespuesta.USUARIO_NO_ENCONTRADO.getLlave());
		}
		return UsuarioMapper.convertirUsuarioADto(proveedor.crearGuardarUsuario(validacionActualizarClave(modeloUsuario, usuario.get())));
	}

	/**
	 * Encontrar Usuario por id
	 *
	 * @param modeloUsuarioId {@link ModeloUsuario}
	 * @return {@link UsuarioDto}
	 */
	public UsuarioDto encontrarUsuarioPorId(final Long modeloUsuarioId) {

		Optional<ModeloUsuario> usuario = proveedor.encontrarUsuarioPorId(modeloUsuarioId);

		if (!usuario.isPresent()) {
			throw new ResponseStatusException(HttpStatus.NOT_FOUND, MensajeRespuesta.USUARIO_NO_ENCONTRADO.getLlave());
		}
		return UsuarioMapper.convertirUsuarioADto(usuario.get());
	}

	public ModeloUsuario encontrarUsuarioPorIdM(final Long modeloUsuarioId) {

		Optional<ModeloUsuario> usuario = proveedor.encontrarUsuarioPorId(modeloUsuarioId);

		if (!usuario.isPresent()) {
			throw new ResponseStatusException(HttpStatus.NOT_FOUND, MensajeRespuesta.USUARIO_NO_ENCONTRADO.getLlave());
		}
		return usuario.get();
	}

	/**
	 * Encontrar Usuarios
	 *
	 * @return {@link List<ModeloUsuario>}
	 */
	public List<UsuarioDto> obtenerUsuarios() {

		List<UsuarioDto> list = new ArrayList<>();

		for (ModeloUsuario m: proveedor.obtenerUsuarios()) {
			list.add(UsuarioMapper.convertirUsuarioADto(m));
		}
		return list;
	}

	/**
	 * Encuentra un usuario por correo
	 *
	 * @param correo {@link ModeloUsuario}
	 * @return {@link ModeloUsuario}
	 */
	public UsuarioDto obtenerUsuarioPorCorreo(final String correo) {

		Optional<ModeloUsuario> usuario = proveedor.encontrarUsuarioPorCorreo(correo);

		if (!usuario.isPresent()) {
			throw new ResponseStatusException(HttpStatus.NOT_FOUND, MensajeRespuesta.USUARIO_NO_ENCONTRADO.getLlave());
		}
		if (Boolean.FALSE.equals(usuario.get().getHabilitado())) {
			throw new ResponseStatusException(HttpStatus.FORBIDDEN, MensajeRespuesta.USUARIO_NO_HABILITADO.getLlave());
		}
		return UsuarioMapper.convertirUsuarioADto(usuario.get()) ;
	}

	public ModeloUsuario obtenerUsuarioPorCorreoM(final String correo) {

		Optional<ModeloUsuario> usuario = proveedor.encontrarUsuarioPorCorreo(correo);

		if (!usuario.isPresent()) {
			throw new ResponseStatusException(HttpStatus.NOT_FOUND, MensajeRespuesta.USUARIO_NO_ENCONTRADO.getLlave());
		}
		if (Boolean.FALSE.equals(usuario.get().getHabilitado())) {
			throw new ResponseStatusException(HttpStatus.FORBIDDEN, MensajeRespuesta.USUARIO_NO_HABILITADO.getLlave());
		}
		return usuario.get() ;
	}

	/**
	 * Inicia la sesion
	 *
	 * @param modeloUsuario {@link ModeloUsuario}
	 * @return {@link ModeloUsuario}
	 */
	public UsuarioDto iniciarSesion(final ModeloUsuario modeloUsuario) {

		Optional<ModeloUsuario> usuario = proveedor.encontrarUsuarioPorCorreo(modeloUsuario);

		if (!usuario.isPresent()) {
			throw new ResponseStatusException(HttpStatus.NOT_FOUND, MensajeRespuesta.USUARIO_NO_ENCONTRADO.getLlave());
		}
		if (Boolean.FALSE.equals(usuario.get().getHabilitado())) {
			throw new ResponseStatusException(HttpStatus.FORBIDDEN, MensajeRespuesta.USUARIO_NO_HABILITADO.getLlave());
		}
		validarClave(modeloUsuario,usuario.get());
		return UsuarioMapper.convertirUsuarioADto(usuario.get());
	}


	private void validarClave(final ModeloUsuario modeloUsuarioEntrada,
								final ModeloUsuario modeloUsuarioObtenido){
		if( !encoder.matches(modeloUsuarioEntrada.getClave(), modeloUsuarioObtenido.getClave()) ){
			throw new ResponseStatusException(HttpStatus.FORBIDDEN, MensajeRespuesta.CLAVE_ERRONEA.getLlave());
		}

	}

	/**
	 * Valida los campos del usuario que se deben ser actualizados
	 */
	private ModeloUsuario validacionActualizarUsuarioPorAdmin(final ModeloUsuario modeloUsuarioEntrada,
															  ModeloUsuario modeloUsuarioActualizar) {

		if (!isNull(modeloUsuarioEntrada.getNombre())) {
			modeloUsuarioActualizar.setNombre(modeloUsuarioEntrada.getNombre());
		}
		if (!isNull(modeloUsuarioEntrada.getCorreo())) {
			modeloUsuarioActualizar.setCorreo(modeloUsuarioEntrada.getCorreo());
		}
		if (!isNull(modeloUsuarioEntrada.getAdministrador())) {
			modeloUsuarioActualizar.setAdministrador(modeloUsuarioEntrada.getAdministrador());
		}
		if (!isNull(modeloUsuarioEntrada.getHabilitado())) {
			modeloUsuarioActualizar.setHabilitado(modeloUsuarioEntrada.getHabilitado());
		}
		return modeloUsuarioActualizar;
	}

	/**
	 * Valida los campos del usuario que se deben ser actualizados
	 */
	private ModeloUsuario validacionActualizarClave(final ModeloUsuario modeloUsuarioEntrada,
													ModeloUsuario modeloUsuarioActualizar) {

		if (!isNull(modeloUsuarioEntrada.getClave())) {
			modeloUsuarioActualizar.setClave(encoder.encode(modeloUsuarioEntrada.getClave()));
		}
		return modeloUsuarioActualizar;
	}

}
