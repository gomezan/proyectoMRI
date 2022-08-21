package com.backend.applicaiton_backend.configuracion;

import org.springframework.boot.autoconfigure.domain.EntityScan;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;
import com.backend.applicaiton_backend.infraestructura.proveedores.ProveedorUsuario;
import com.backend.applicaiton_backend.infraestructura.proveedores.ProveedorImagen;
import com.backend.applicaiton_backend.infraestructura.repositorio.RepositorioUsuario;
import com.backend.applicaiton_backend.infraestructura.repositorio.RepositorioImagen;

/**
 * A configuration class in charge of the providers' setup.
 *
 * @author <a href="santiagoromero@javeriana.edu.co.com"> Santiago Romero </a>
 * @since 1.0.0
 */
@Configuration
@EntityScan("com.backend.applicaiton_backend.infraestructura.modelo")
@EnableJpaRepositories("com.backend.applicaiton_backend.infraestructura.repositorio")
public class ConfiguracionProveedores {

	/**
	 * A {@link ProveedorUsuario} implementacion que necesita  {@link RepositorioUsuario}.
	 *
	 * @param repositorio {@link RepositorioUsuario} implementacion.
	 * @return un {@link ProveedorUsuario} implementacion.
	 */
	@Bean
	public ProveedorUsuario proveedorUsuario(final RepositorioUsuario repositorio) {

		return new ProveedorUsuario(repositorio);
	}

	/**
	 * A {@link ProveedorImagen} implementacion que necesita  {@link RepositorioImagen}.
	 *
	 * @param repositorio {@link RepositorioImagen} implementacion.
	 * @return un {@link ProveedorUsuario} implementacion.
	 */
	@Bean
	public ProveedorImagen proveedorImagen(final RepositorioImagen repositorio) {

		return new ProveedorImagen(repositorio);
	}

}
