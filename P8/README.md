# P8 - Display OLED con Logo

## Descripción
Esta práctica introduce el uso de pantallas OLED (Organic Light Emitting Diode) para mostrar contenido gráfico incluyendo logos y símbolos personalizados.

## Objetivos
- Entender las diferencias entre LCD y OLED
- Configurar pantallas OLED I2C/SPI
- Crear y mostrar gráficos y logos
- Implementar animaciones básicas

## Requisitos
- Raspberry Pi
- Pantalla OLED (128x64 típicamente)
- Librerías PIL (Pillow) y Adafruit

## Contenido
- **P8-OLED-LOGO.odt**: Documentación con guía de gráficos
- **P8_oled_display_project/**: Proyecto con ejemplos de logos

## Ventajas del OLED
- Mejor contraste y colores vibrantes
- Mayor resolución que LCD
- Menor consumo de energía
- Ángulo de visión superior

## Conexión Típica I2C
```
GND  -----> GND
VCC  -----> 3.3V
SCL  -----> GPIO 3 (I2C SCL)
SDA  -----> GPIO 2 (I2C SDA)
```

## Formato de Imágenes
- Formato: PNG o BMP en escala de grises
- Resolución: 128x64 pixeles
- Conversión a matriz de bits para OLED
