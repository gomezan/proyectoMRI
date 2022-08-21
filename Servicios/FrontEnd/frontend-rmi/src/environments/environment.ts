// This file can be replaced during build by using the `fileReplacements` array.
// `ng build` replaces `environment.ts` with `environment.prod.ts`.
// The list of file replacements can be found in `angular.json`.

/**
   * Contiene: 
   * -Nombre del bucket donde están las imágenes
   * -Carpeta de imágenes no procesadas
   * -Carpeta de imágenes procesadas
   * -Región del bucket
   * -Clave de acceso
   * -Clave secreta
   * -URL de S3
   * -Control de acceso de origen
   * -URL del Back-End
   * -Versión de la API de AWS S3
   */
export const environment = {
  production: false,
  AWS_ACCESS_KEY_ID : 'AKIAVZASHVKLQFWOYP6X',
  AWS_ACCESS_KEY_SECRET : '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',
  REGION_NAME : 'sa-east-1',
  BUCKET_NAME : 'imagenes-tesis',
  IMAGENES_PROCESADAS : 'procesada',
  IMAGENES_NO_PROCESADAS : 'no_procesada',
  RESOURCE : 's3',
  URL_BACKEND_BASE : "http://localhost:8080",
  URL_AWS_S3: 'https://imagenes-tesis.s3.amazonaws.com/',
  AWS_S3_API_VERSION: '2006-03-01',
  ACCESS_CONTROL_ALLOW_ORIGIN: 'http://localhost:4200',
  REGEX_CORREO: /^[\w\-\.]{3,20}@[a-z]{2,10}((\.[a-z]{2,5}){1,3})$/g,
  REGEX_NOMBRE: /^([A-ZÀ-Ö\u00d1][a-zà-ÿ\u00f1]{2,15}\s){1,4}([A-ZÀ-Ö\u00d1][a-zà-ÿ\u00f1]{3,15})$/g,
  REGEX_CONTRASENA: /^[\w\.\-]{3,30}$/g,
  REGEX_OBSERVACION: /^(([\wÀ-ÿ]{1,10}\s){0,5})[\wÀ-ÿ]{1,10}$/g
};

/*
 URL_AWS_S3: "https://jgm-imagen-tesis.s3.amazonaws.com/"
 "https://jgm-imagen-tesis.s3.sa-east-1.amazonaws.com/no_procesada"
 * For easier debugging in development mode, you can import the following file
 * to ignore zone related error stack frames such as `zone.run`, `zoneDelegate.invokeTask`.
 *
 * This import should be commented out in production mode because it will have a negative impact
 * on performance if an error is thrown.
 */
// import 'zone.js/plugins/zone-error';  // Included with Angular CLI.