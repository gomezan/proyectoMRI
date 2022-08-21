package com.backend.applicaiton_backend.presentacion.security;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.stereotype.Service;
import com.backend.applicaiton_backend.infraestructura.modelo.ModeloUsuario;
import com.backend.applicaiton_backend.logicanegocio.casosuso.GestionaUsuarioCU;
import lombok.extern.slf4j.Slf4j;

@Service  // ~ @Component
@Slf4j
public class CustomUserDetailsService implements UserDetailsService {

	@Autowired
	private GestionaUsuarioCU casoUso;

	@Override
	public UserDetails loadUserByUsername(String correo) {

		log.info("loading user");
		ModeloUsuario usuario = casoUso.obtenerUsuarioPorCorreoM(correo);
		return new CustomUserDetails(usuario);
	}

}