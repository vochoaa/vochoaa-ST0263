# ST02363 Tópicos Especiales en Telemática
#
# Valentina Ochoa Arboleda, vochoaa@eafit.edu.co
#
# Profesor:Edwin Nelson Montoya Múnera, emontoya@eafit.edu.co
#
# 
# Reto 2
#
# 1. breve descripción de la actividad
#
  Este  reto consiste en realizar 3 componentes principales.
  ## 1. Microservicio 1##  
  Este esta encargado de listar archivos a través de gRPC.Realiza la comunicación con el API Gateway.
  ## 2. Microservicio 2
  Este esta encargado de buscar archivos mediante una query a través de MOM (RabbitMQ). Realiza la comunicación con el API Gateway.
  ## 3. Microservicio API Gateway
  Encargado de funcionar tanto como gateway como balanceador de cargas y proxy.
  
## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.
El cliente inicia solicitudes, que pueden originarse tanto en su navegador web como en Postman. Estas solicitudes se comunican a través de una API REST. Luego, el API Gateway establece una comunicación gRPC con el primer microservicio, que tiene la responsabilidad de listar archivos. Por otro lado, el segundo microservicio se comunica a través de un mecanismo de mensajería orientada a eventos (MOM) utilizando RabbitMQ. Este microservicio opera mediante colas y su función principal es buscar archivos basados en las consultas proporcionadas por el usuario. La elección entre estos dos modos de comunicación depende del tipo de solicitud realizada por el cliente.

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.
Todos los servicios fueron implementados con Python 3.10.6. Además se incluyeron las siguientes librerías que ayudaron al correcto funcionamiento del reto: 

  Flask==2.2.3
  grpc==1.0.0
  grpcio==1.51.3
  pika==1.3.1
  protobuf==4.22.0
  python-dotenv==1.0.

## como se compila y ejecuta.
## detalles del desarrollo.
## detalles técnicos
## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
 
# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

# IP o nombres de dominio en nube o en la máquina servidor.

## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)

## como se lanza el servidor.

## una mini guia de como un usuario utilizaría el software o la aplicación

## opcionalmente - si quiere mostrar resultados o pantallazos 

# 5. otra información que considere relevante para esta actividad.

# referencias:
<debemos siempre reconocer los créditos de partes del código que reutilizaremos, así como referencias a youtube, o referencias bibliográficas utilizadas para desarrollar el proyecto o la actividad>
## sitio1-url 
## sitio2-url
## url de donde tomo info para desarrollar este proyecto

#### versión README.md -> 1.0 (2022-agosto)
