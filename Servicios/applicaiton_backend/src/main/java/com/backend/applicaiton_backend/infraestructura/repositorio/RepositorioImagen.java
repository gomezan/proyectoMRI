package com.backend.applicaiton_backend.infraestructura.repositorio;

import java.util.List;

import javax.transaction.Transactional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import com.backend.applicaiton_backend.infraestructura.modelo.ModeloImagen;
import com.backend.applicaiton_backend.infraestructura.modelo.ModeloUsuario;

/**
 * Provee sofisticadas funcionalidades CRUD para la clase {@link ModeloImagen}  que es gestionada.
 *
 * @author <a href="santiagoromero@javeriana.edu.co"> Santiago Romero </a>
 * @since 1.0.0
 */
@Transactional
public interface RepositorioImagen extends JpaRepository<ModeloImagen, Long> {

	//Optional<ModeloImagen> findByIdAndUsuario(Long imagenId, Long usuario);

	List<ModeloImagen> findAllByUsuario(ModeloUsuario usuario);

	@Query(value = "select * from tesis.imagen i where i.estado = 'SUBIDO' order by i.fecha_inicial  asc  limit 1", nativeQuery = true)
	ModeloImagen obtenerSiguienteImagen();

	@Modifying @Query(value = "update  tesis.imagen set estado  = 'ELIMINADO' where estado <> 'ELIMINADO' and fecha_eliminacion <  CURRENT_DATE;", nativeQuery = true)
	void eliminarImagenes();


}
