# P6 - LCD con Sensor DHT11

## Descripción
Esta práctica integra la pantalla LCD con el sensor DHT11 para crear un sistema de visualización de datos ambientales en tiempo real.

## Objetivos
- Integrar múltiples componentes en un solo proyecto
- Mostrar datos de temperatura y humedad en la pantalla LCD
- Implementar actualizaciones periódicas de datos
- Manejar la visualización eficiente en pantalla de 16 caracteres

## Requisitos
- Raspberry Pi
- Pantalla LCD (16x2)
- Sensor DHT11
- Librerías para LCD y DHT11

## Contenido
- **P6-LCD-DHT11.odt**: Documentación del proyecto completo
- **P6_dht_lcd_project/**: Código del proyecto integrado

## Características Principales
- Lectura continua del sensor DHT11
- Visualización en tiempo real en LCD
- Formateo automático de datos en pantalla
- Control de actualización de pantalla

## Distribución en Pantalla LCD
```
Línea 1: Temp: XX°C
Línea 2: Hum:  XX%
```

## Notas de Implementación
- Usar hilos (threads) para lecturas no bloqueantes
- Implementar manejo de excepciones
- Considerar tiempo de actualización óptimo
