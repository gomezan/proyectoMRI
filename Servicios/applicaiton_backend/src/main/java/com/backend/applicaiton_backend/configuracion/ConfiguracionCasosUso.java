package com.backend.applicaiton_backend.configuracion;

import org.springframework.boot.context.properties.EnableConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import com.backend.applicaiton_backend.infraestructura.proveedores.ProveedorImagen;
import com.backend.applicaiton_backend.infraestructura.proveedores.ProveedorUsuario;
import com.backend.applicaiton_backend.logicanegocio.casosuso.GestionaUsuarioCU;
import com.backend.applicaiton_backend.logicanegocio.casosuso.GestionaImagenCU;

/**
 * configuracion de los casos de uso.
 *
 * @author <a href="santiagoromero@javeriana.edu.co"> Santiago Romero </a>
 * @since 1.0.0
 */
@Configuration
@EnableConfigurationProperties
@ComponentScan("com.backend.applicaiton_backend")

public class ConfiguracionCasosUso {

	/**
	 * A {@link GestionaUsuarioCU} implementacion que necesita  {@link ProveedorUsuario}.
	 *
	 * @param proveedor {@link ProveedorUsuario} implementacion.
	 * @return un {@link GestionaUsuarioCU} implementacion.
	 */
	@Bean
	public GestionaUsuarioCU gestionaUsuario(final ProveedorUsuario proveedor) {

		return new GestionaUsuarioCU(proveedor);
	}

	/**
	 * A {@link GestionaImagenCU} implementacion que necesita  {@link ProveedorImagen}.
	 *
	 * @param proveedor {@link ProveedorImagen} implementacion.
	 * @return un {@link GestionaImagenCU} implementacion.
	 */
	@Bean
	public GestionaImagenCU gestionaImagen(final ProveedorImagen proveedor) {

		return new GestionaImagenCU(proveedor);
	}
}
