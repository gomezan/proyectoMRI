package com.backend.applicaiton_backend.infraestructura.repositorio;

import java.util.List;
import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import com.backend.applicaiton_backend.infraestructura.modelo.ModeloUsuario;

/**
 * Provee sofisticadas funcionalidades CRUD para la clase {@link ModeloUsuario}  que es gestionada.
 *
 * @author <a href="santiagoromero@javeriana.edu.co"> Santiago Romero </a>
 * @since 1.0.0
 */
public interface RepositorioUsuario extends JpaRepository<ModeloUsuario, Long> {

	Optional<ModeloUsuario> findByCorreo(String correo);

	@Query(value = "select * from tesis.usuario u where u.administrador = false", nativeQuery = true)
	List<ModeloUsuario> encontrarUsuariosDiferentesAdmin();
}
