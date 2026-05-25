# P13 - QUEUE QoS MQTT REDIS y SQLite

## Descripción
Esta práctica avanzada implementa un sistema completo de IoT con protocolo MQTT, manejo de colas, almacenamiento en bases de datos y caché distribuido.

## Objetivos
- Configurar broker MQTT (Mosquitto)
- Implementar publicador/suscriptor MQTT
- Usar Redis para caché distribuido
- Almacenar datos en SQLite
- Implementar niveles de QoS

## Requisitos
- Raspberry Pi
- Servidor MQTT (Mosquitto) instalado
- Redis instalado
- Python con bibliotecas paho-mqtt, redis, sqlite3
- Sensor DHT11

## Contenido
- **P13 - QUEUE QoS MQTT REDIS y SQLite.odt**: Documentación completa
- **P13/**: Código del servidor y cliente
- **mosquito/**: Configuración de Mosquitto

## Componentes del Sistema

### MQTT (Message Queuing Telemetry Transport)
- Protocolo ligero para IoT
- Publicador/Suscriptor
- Niveles QoS: 0, 1, 2

### Redis
- Base de datos en memoria
- Caché de datos recientes
- Muy rápido para lecturas frecuentes

### SQLite
- Base de datos relacional
- Almacenamiento persistente
- Análisis histórico

## Arquitectura
```
Sensor DHT11
    |
    v
Publicador MQTT
    |
    v
Broker Mosquitto
    |
    +-----> Suscriptor (almacena en Redis y SQLite)
    +-----> Otros clientes MQTT
```

## Configuración MQTT
```
Topics:
  - sensor/temperatura
  - sensor/humedad
  - sensor/estado

QoS Levels:
  - 0: At most once (máximo una vez)
  - 1: At least once (al menos una vez)
  - 2: Exactly once (exactamente una vez)
```

## Almacenamiento
- Redis: Últimos 100 valores
- SQLite: Histórico completo con timestamp

## Notas de Seguridad
- Configurar autenticación en Mosquitto
- Usar contraseñas seguras
- Considerar encriptación TLS/SSL
