# P5 - Sensor DHT11

## Descripción
Esta práctica aborda el uso del sensor de temperatura y humedad DHT11 con Raspberry Pi. Se aprenderá a leer datos analógicos del sensor y procesarlos correctamente.

## Objetivos
- Entender el funcionamiento del sensor DHT11
- Configurar la lectura de datos del sensor
- Procesar y calibrar mediciones de temperatura y humedad
- Implementar manejo de errores en lecturas

## Requisitos
- Raspberry Pi
- Sensor DHT11
- Resistencia pull-up (típicamente 4.7kΩ)
- Librerías Adafruit_DHT o similar

## Contenido
- **P5-DHT11.odt**: Documentación detallada con especificaciones del sensor
- **P5_dht11_lab/**: Laboratorio con ejemplos de código

## Especificaciones del DHT11
- Rango de temperatura: 0-50°C
- Rango de humedad: 20-80%
- Precisión: ±2°C y ±5%
- Tiempo de respuesta: ~2 segundos

## Conexión
```
GND    -----> GND (Pin 6)
DATA   -----> GPIO 4 (Pin 7)
VCC    -----> 3.3V (Pin 1)
```

## Consideraciones
- El sensor requiere una resistencia pull-up en el pin de datos
- Espaciar lecturas al menos 2 segundos
- Validar datos antes de usarlos
