package com.backend.applicaiton_backend.presentacion.stream;

import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;

import org.springframework.jms.annotation.JmsListener;
import org.springframework.stereotype.Component;
import org.springframework.web.bind.annotation.RestController;
import com.backend.applicaiton_backend.logicanegocio.casosuso.GestionaImagenCU;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

/**
 * Consumidor de los mensajes de la cola provenientes del sistema modelo Principalmente son mensajes de actualizacion de los datos de la
 * imagen
 *
 * @author <a href="santiagoromero@javeriana.edu.co"> Santiago Romero </a>
 * @since 1.0.0
 */

@Component
@Slf4j
@RestController
@RequiredArgsConstructor
public class ConsumidorActiveMQ {

	/**
	 * Caso de uso gestionar imagen
	 */
	private final GestionaImagenCU gestionaImagenCU;

	@JmsListener(destination = "${spring.activemq.nombre-cola}")
	public void consumeActiveMQ(byte[] imagen) throws JsonProcessingException {

		String json = new String(imagen, StandardCharsets.UTF_8);
		Map<String, Object> mapa = new Gson().fromJson(json, new TypeToken<HashMap<String, Object>>() {}.getType());
		log.info("imagen obtenida para actualizar: {}", mapa.toString());
		gestionaImagenCU.actualizarImagenCola(mapa);


	}
}
