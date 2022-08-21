package com.backend.applicaiton_backend.presentacion.security;

import java.util.Collection;
import java.util.List;

import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;
import com.backend.applicaiton_backend.infraestructura.modelo.ModeloUsuario;

public class CustomUserDetails implements UserDetails {

	final private ModeloUsuario usuario;

	public enum Role {ADMIN, OTHER}

	public CustomUserDetails(final ModeloUsuario usuario) {

		this.usuario = usuario;
	}

	@Override
	public Collection<? extends GrantedAuthority> getAuthorities() {

		if (Boolean.TRUE.equals(usuario.getAdministrador())) {
			return List.of(new SimpleGrantedAuthority(Role.ADMIN.name()));
		}
		return List.of(new SimpleGrantedAuthority(Role.OTHER.name()));

	}

	@Override
	public String getPassword() {

		return usuario.getClave();
	}

	@Override
	public String getUsername() {

		return usuario.getCorreo();
	}

	@Override
	public boolean isAccountNonExpired() {

		return true;
	}

	@Override
	public boolean isAccountNonLocked() {

		return true;
	}

	@Override
	public boolean isCredentialsNonExpired() {

		return true;
	}

	@Override
	public boolean isEnabled() {

		return true;
	}

}
