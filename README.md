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
  # 1. Microservicio 1
  Este esta encargado de listar archivos a través de gRPC.Realiza la comunicación con el API Gateway.
  ## 2. Microservicio 2
  Este esta encargado de buscar archivos mediante una query a través de MOM (RabbitMQ). Realiza la comunicación con el API Gateway.
  ## 3. Microservicio API Gateway
  Encargado de funcionar tanto como gateway como balanceador de cargas y proxy.
## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
Se implementando el microservicio 1, el microservicio 2 y el microservicio API Gateway y la comunicación vía gRPC para el microservicio 1.
## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
No se logro la comunicación vía MOM (RabbitMQ) para el microservicio 2.
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
## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
Cada microservicio cuenta con su .env, donde:
## Gateway:
HOST_GRPC=localhost

PORT_GRPC=50051

HOST_RMQ=localhost

PORT_RMQ=5672

USER=guest

PASSWORD=guest

QUEUE="archivo_rpc"

## GRPC-Ser1:
PORT_GRPC=50051
## MOM-Ser2:
HOST_RMQ=localhost

PORT_RMQ=5672

USER=guest

PASSWORD=guest

QUEUE="archivo_rpc"
 
# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.
Se utiliza el mismo lenguaje, librerías, paquetes y demás que en el ambiente de desarrollo.
# IP o nombres de dominio en nube o en la máquina servidor.
No se utiliza ip elestica ya que no fue subido a la nube. 
Se utiliza el local host.
## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
Se configuran de la misma manera con los archivos .env.

## una mini guia de como un usuario utilizaría el software o la aplicación

# referencias:
https://grpc.io/docs/languages/python/basics/
## url de donde tomo info para desarrollar este proyecto
https://github.com/st0263eafit/st0263-232
#### versión README.md -> 1.0 (2023-agosto)
