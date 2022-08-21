package com.backend.applicaiton_backend.configuracion;

import javax.jms.ConnectionFactory;
import javax.jms.Queue;

import org.apache.activemq.ActiveMQConnectionFactory;
import org.apache.activemq.command.ActiveMQQueue;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Primary;
import org.springframework.jms.annotation.EnableJms;
import org.springframework.jms.config.DefaultJmsListenerContainerFactory;

@EnableJms
@Configuration
public class ConfiguracionActiveMQ {

	/**
	 * url del broker donde se encuentra la cola
	 */
	@Value("${spring.activemq.broker-url}")
	private String brokerUrl;

	@Value("${spring.activemq.nombre-cola}")
	public String PAYS_QUEUE_NAME;

	@Bean
	@Primary
	public Queue paysQueue(){
		return new ActiveMQQueue(PAYS_QUEUE_NAME);
	}

	@Bean
	@Primary
	public ActiveMQConnectionFactory activeMQConnectionFactory(){
		ActiveMQConnectionFactory conexion = new ActiveMQConnectionFactory();
		conexion.setBrokerURL(brokerUrl);
		return conexion;
	}

	@Bean
	public DefaultJmsListenerContainerFactory jmsListenerContainerFactory(ConnectionFactory connectionFactory) {
		DefaultJmsListenerContainerFactory factory = new DefaultJmsListenerContainerFactory();
		factory.setConnectionFactory(connectionFactory);
		return factory;
	}


}
