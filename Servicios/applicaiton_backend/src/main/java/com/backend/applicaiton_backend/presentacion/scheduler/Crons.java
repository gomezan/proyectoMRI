package com.backend.applicaiton_backend.presentacion.scheduler;

import java.text.SimpleDateFormat;
import java.util.Date;

import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;
import com.backend.applicaiton_backend.logicanegocio.casosuso.GestionaImagenCU;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

@Component
@RequiredArgsConstructor
@Slf4j
public class Crons {

	/**
	 * Caso de uso gestionar imagen
	 */
	private final GestionaImagenCU gestionaImagenCU;


	@Scheduled(cron = " 0 0 0 * * *")
	public void eliminarImagenes() {
		SimpleDateFormat formatter = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
		Date date = new Date();
		//descomentar al momento de ser necesitada la eliminación a base de datos
		//gestionaImagenCU.eliminarImagenes();
		log.info("Cron de eliminacion de imagenes ejecutado a las: {}", formatter.format(date));
	}


}
