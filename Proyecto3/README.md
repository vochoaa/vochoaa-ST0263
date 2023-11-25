# ST02363 Tópicos Especiales en Telemática

# Estudiantes: Valentina Ochoa Arbooleda, vochoaa@eafit.edu.co
# Brigth Lorena Giraldo Vargas, blgiraldov@eafit.edu 
# Katherine Benjumena Ortiz, kbenjumeao@efit.edu.co

# Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co

# Proyecto 3
# 1. breve descripción de la actividad
# Proyecto de streaming para la captura de datos en tiempo real.

El objetivo de este sistema es capturar datos en tiempo real provenientes del mercado de valores y procesarlos de manera eficiente y en tiempo real. La arquitectura está diseñada para integrar tecnologías clave, como Apache Kafka para la ingestión de datos en streaming, una base de datos NoSQL para el almacenamiento persistente, y un procesador de flujos para análisis en tiempo real de los datos financieros.

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)


## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

Todos los aspectos se cumplieron. 

# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.
El proyecto sigue una arquitectura de streaming de datos desde el servidor WebSocket de Finnhub hacia Apache Kafka, utilizando un script Python llamado TradesStreaming. Este script se conecta al servidor WebSocket, suscribe símbolos de "ticker" específicos y envía las actualizaciones en tiempo real al tema "raw_data" en Kafka. Desde Kafka, los datos pueden ser consumidos por otros procesadores en tiempo real para análisis y también son almacenados de forma persistente en MongoDB para su posterior consulta y análisis retrospectivo. El proyecto prioriza la escalabilidad, durabilidad y flexibilidad en el análisis de datos financieros provenientes del mercado de valores


# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

Se realizó en GCP, utilizando databricks para realizar el pipeline que consume de apache Kafka.

Se utilizaron archivos yaml
1. Kafka.yaml  Este archivo define los servicios de Docker para ejecutar Kafka y Zookeeper. Se utiliza la imagen oficial de Confluent para Kafka y Zookeeper. Se especifican los puertos expuestos y las configuraciones necesarias para la comunicación entre Kafka y Zookeeper.

2. MongoDb.yaml Este archivo de configuración Docker establece el servicio de MongoDB. Se utiliza la imagen oficial de MongoDB con la versión 3.8. Se especifican las credenciales de inicio de sesión y se mapean los puertos para la comunicación con la base de datos.

Se utilizó pyhton con las siguientes librerías:


Se utilizó MongoDB para la base de datos.

## como se compila y ejecuta.

Se debe instalar Python.
Se debe de clonar el repositorio.


## detalles del desarrollo.



## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)

Ip: 104.197.171.58::27017 -> Base de datos
Ip:  104.197.171.58::9092-> Apache Kafka 

# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.


## opcionalmente - si quiere mostrar resultados o pantallazos


# 5. otra información que considere relevante para esta actividad.

# referencias:

## https://learn.microsoft.com/es-es/windows/win32/directshow/about-the-multimedia-streaming-architecture
## https://kafka.apache.org/
## https://avi-soori.medium.com/databricks-automl-sql-streaming-ml-on-the-lakehouse-6ea1aa1fcd18
## https://docs.databricks.com/en/structured-streaming/index.html

#### versión README.md -> 1.0 (2023-noviembre)
