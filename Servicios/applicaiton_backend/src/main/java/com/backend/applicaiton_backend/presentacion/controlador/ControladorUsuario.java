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
import com.backend.applicaiton_backend.infraestructura.modelo.ModeloUsuario;
import com.backend.applicaiton_backend.logicanegocio.DTO.UsuarioDto;
import com.backend.applicaiton_backend.logicanegocio.casosuso.GestionaUsuarioCU;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

/**
 * Controlador usuario
 *
 * @author <a href="santiagoromero@javeriana.edu.co"> Santiago Romero </a>
 * @since 1.0.0
 */
@Slf4j
@RestController
@RequiredArgsConstructor
@RequestMapping("/usuario")
public class ControladorUsuario {

	/**
	 * Caso de uso gestionar usuario
	 */
	private final GestionaUsuarioCU gestionaUsuarioCU;

	/**
	 * Crea un  usuario
	 *
	 * @param usuario {@link ModeloUsuario}
	 */
	@PostMapping("/crear_usuario")
	public ResponseEntity<UsuarioDto> crearUsuario(@RequestBody ModeloUsuario usuario){
		return new ResponseEntity<>(gestionaUsuarioCU.crearUsuario(usuario), HttpStatus.CREATED);
	}

	/**
	 * Actualiza los datos de un usuario por el administrador
	 *
	 * @param usuario {@link ModeloUsuario}
	 */
	@PutMapping("/actualizar_usuario_admin")
	public ResponseEntity<UsuarioDto> actualizarUsuarioPorAdmin(@RequestBody ModeloUsuario usuario){

		return new ResponseEntity<>(gestionaUsuarioCU.actualizarUsuarioPorAdmin(usuario), HttpStatus.OK);
	}

	/**
	 * Actualiza un la clave por un usuario
	 *
	 * @param usuario {@link ModeloUsuario}
	 */
	@PutMapping("/actualizar_clave")
	public ResponseEntity<UsuarioDto> actualizarClave(@RequestBody ModeloUsuario usuario){

		return new ResponseEntity<>(gestionaUsuarioCU.actualizarClaveUsuario(usuario), HttpStatus.OK);
	}

	/**
	 * Inicia sesion
	 *
	 * @param usuario {@link ModeloUsuario}
	 */
	//@CrossOrigin(origins = "http://localhost:8080")
	@PostMapping("/iniciar_sesion")
	public ResponseEntity<UsuarioDto> iniciarSesion(@RequestBody ModeloUsuario usuario){

		return new ResponseEntity<>(gestionaUsuarioCU.iniciarSesion(usuario), HttpStatus.OK);
	}

	/**
	 * encontrar usuario
	 *
	 * @param usuarioId {@link ModeloUsuario}
	 */
	@GetMapping("/encontrar_usuario/{usuarioId}")
	public ResponseEntity<UsuarioDto> encontrarUsuario(@PathVariable Long usuarioId){

		return new ResponseEntity<>(gestionaUsuarioCU.encontrarUsuarioPorId(usuarioId), HttpStatus.OK);
	}

	/**
	 * obtiene todos los usuarios para que e admin modifique los datos
	 *
	 */
	@GetMapping("/obtener_usuarios_diferentes_al_admin")
	public ResponseEntity<List<UsuarioDto>> obtenerUsuarios(){
		return new ResponseEntity<>(gestionaUsuarioCU.obtenerUsuarios(), HttpStatus.OK);
	}




}
