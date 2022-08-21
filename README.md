# SISTEMA DE APOYO PARA SUPER-RESOLUCIÓN DE IMÁGENES DE RESONANCIA MAGNÉTICA USANDO TÉCNICAS DE APRENDIZAJE PROFUNDO (Proyecto de grado)

## Abstract
In modern medicine, magnetic resonance images are essential for diagnosing a patient, nevertheless, a problem many hospitals face is the difficulty of obtaining high resolution images due to high-cost factors. The present project aims to solve this problem through the development of a web application that increases image spatial resolution through a super-resolution algorithm trained over a DCSRN neural network. The application is composed of a Front-End system constructed following MVC architecture using Angular, a Back-End system constructed following Multi-level architecture using Spring-Boot, and a Model system written in Python following Component architecture. 

### Pre-requisitos
Antes de correr e sistema completo es necesario tener instalado:
* Versión de python mayor a 3.7
* ActiveMQ
* Angular
* Postgres SQL
* Java 11
* Maven


###### AWS S3 ######

---- Permisos en un Bucket S3 ----

--- Bloquear acceso público (configuración del bucket) ---

Bloquear el acceso público a buckets y objetos concedido a través de cualquier lista de control de acceso (ACL)

Bloquear el acceso público y entre cuentas a buckets y objetos concedido a través de cualquier política de bucket y puntos de acceso pública

--- Política de bucket ---

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Principal": {
                "AWS": "*"
            },
            "Action": [
                "s3:PutObject",
                "s3:PutObjectAcl",
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::imagenes-tesis/no_procesada/*",
                "arn:aws:s3:::imagenes-tesis/procesada/*"
            ]
        }
    ]
}


--- Propiedad del objeto ---
ACL habilitadas

Escritor de objetos

--- Lista de control de acceso (ACL) ---
Solo el dueño de la cuenta tiene permisos de Escritura y Lectura sobre Objetos y ACLs

--- Uso compartido de recursos entre orígenes (CORS) ---

[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "POST",
            "GET",
            "PUT",
            "HEAD"
        ],
        "AllowedOrigins": [
            "http://localhost:4200"
        ],
        "ExposeHeaders": [
            "Content-Length",
            "Content-Type",
            "Date",
            "Server",
            "x-amz-delete-marker",
            "x-amz-id-2",
            "x-amz-request-id"
        ],
        "MaxAgeSeconds": 3000
    }
]


### Correr ActiveMQ

`activemq start`

### Correr el front

Dirigirse a la siguiente carpeta

`cd Servicios/FrontEnd/frontend-rmi/`

En esta carpeta ejecutar

`ng serve`

### Correr el back

Dirigirse a la siguiente carpeta

`cd Servicios/applicaiton_backend/`

En esta carpeta ejecutar

`mvn clean install`

Luego, dirigirse a la siguiente carpeta

`cd Servicios/applicaiton_backend/target`

correr:

`java -jar applicaiton_backend-0.0.1-SNAPSHOT.jar`

### Correr el sistema del modelo

Dirigirse a la siguiente carpeta

`cd Servicios/sistemaModelo/`

Correr:

`python main.py`

## Creación del primer usuario

Para poder hacer uso del aplicativo es necesario tener un usuario administrador con el fin de crear usuarios investigadores
para esto, es necesario crrer el siguiente CURL

´curl --location --request POST 'localhost:8080/usuario/crear_usuario' \
--header 'Content-Type: application/json' \
--data-raw '{
    "nombre": "Nombre Ejemplo",
    "correo": "admin@gmail.com",
    "clave": "123",
    "administrador":true,
    "habilitado": true
}'´

Una vez creado el usuario administrador, ya puede empezar a hacer uso del aplicativo navegando por el browser.
