# P4 - LCD Display

## Descripción
Esta práctica se enfoca en el uso y control de pantallas LCD (Liquid Crystal Display) con Raspberry Pi. Se aprenderán los conceptos fundamentales de comunicación con pantallas de cristal líquido y su integración con el sistema.

## Objetivos
- Entender la arquitectura y funcionamiento de pantallas LCD
- Configurar la conexión de una pantalla LCD a Raspberry Pi
- Programar comandos básicos de control y visualización
- Implementar textos y caracteres especiales en pantalla

## Requisitos
- Raspberry Pi
- Pantalla LCD (16x2 o similar)
- Cables de conexión y resistencias
- Librerías Python para control LCD

## Contenido
- **P4-LCD.odt**: Documentación completa con diagramas de conexión y código fuente
- **P4_lcd_project/**: Proyecto con el código implementado

## Notas Importantes
- Verificar los pines GPIO correctamente antes de hacer conexiones
- Utilizar resistencias pull-up si es necesario
- Consultar la documentación específica del modelo de LCD utilizado

## Conexiones Típicas
```
GND -----> GND
VCC -----> 5V
SDA -----> GPIO 2 (SDA)
SCL -----> GPIO 3 (SCL)
```
