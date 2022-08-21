package com.backend.applicaiton_backend;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableScheduling;

@SpringBootApplication
@EnableScheduling
public class ApplicaitonBackendApplication {

	public static void main(String[] args) {
		SpringApplication.run(ApplicaitonBackendApplication.class, args);
	}


}
