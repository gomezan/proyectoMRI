package com.backend.applicaiton_backend.logicanegocio.DTO;

import com.backend.applicaiton_backend.infraestructura.modelo.ModeloUsuario;

public class UsuarioMapper {

	public static UsuarioDto convertirUsuarioADto(ModeloUsuario modeloUsuario) {

		UsuarioDto usuarioDto = new UsuarioDto();
		usuarioDto.setUsuarioId(modeloUsuario.getUsuarioId());
		usuarioDto.setNombre(modeloUsuario.getNombre());
		usuarioDto.setCorreo(modeloUsuario.getCorreo());
		usuarioDto.setAdministrador(modeloUsuario.getAdministrador());
		usuarioDto.setFechaCreacion(modeloUsuario.getFechaCreacion());
		usuarioDto.setHabilitado(modeloUsuario.getHabilitado());
		usuarioDto.setImagenes(modeloUsuario.getImagenes());
		return usuarioDto;

	}

}
